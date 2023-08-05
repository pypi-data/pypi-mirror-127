import logging
import math
from ray import ray_constants
from deltacat import logs
from deltacat.aws.redshift.model import manifest as rsm, \
    manifest_entry as rsme, manifest_meta as rsmm
from deltacat.compute.compactor.model import delta_annotated as da
from deltacat.storage import interface as unimplemented_deltacat_storage
from deltacat.storage.model import list_result as lr, partition_locator as pl,\
    stream_locator as sl, delta as dc_delta
from typing import Any, Dict, List, Optional

logger = logs.configure_deltacat_logger(logging.getLogger(__name__))


def discover_deltas(
        source_partition_locator: Dict[str, Any],
        start_position_exclusive: Optional[int],
        end_position_inclusive: int,
        deltacat_storage=unimplemented_deltacat_storage) \
        -> List[Dict[str, Any]]:

    stream_locator = pl.get_stream_locator(source_partition_locator)
    namespace = sl.get_namespace(stream_locator)
    table_name = sl.get_table_name(stream_locator)
    table_version = sl.get_table_version(stream_locator)
    partition_values = pl.get_partition_values(source_partition_locator)
    deltas_list_result = deltacat_storage.list_deltas(
        namespace,
        table_name,
        partition_values,
        table_version,
        start_position_exclusive,
        end_position_inclusive,
        True,
    )
    deltas = lr.all_items(deltas_list_result)
    if not deltas:
        raise RuntimeError(f"Unexpected Error: Couldn't find any deltas to "
                           f"compact in delta stream position range "
                           f"('{start_position_exclusive}', "
                           f"'{end_position_inclusive}']. Source partition: "
                           f"{source_partition_locator}")
    if start_position_exclusive:
        first_delta = deltas.pop(0)
        logger.info(f"Removed exclusive start delta w/ expected stream "
                    f"position '{start_position_exclusive}' from deltas to "
                    f"compact: {first_delta}")
    logger.info(f"Count of deltas to compact in delta stream "
                f"position range ('{start_position_exclusive}', "
                f"'{end_position_inclusive}']: {len(deltas)}. Source "
                f"partition: '{source_partition_locator}'")
    return deltas


def limit_input_deltas(
        input_deltas: List[Dict[str, Any]],
        cluster_resources: Dict[str, float],
        hash_bucket_count: int,
        user_hash_bucket_chunk_size: int,
        deltacat_storage=unimplemented_deltacat_storage):

    # TODO (pdames): when row counts are available in metadata, use them
    #  instead of bytes - memory consumption depends more on number of
    #  input delta records than bytes.

    # Inflation multiplier from snappy-compressed parquet to pyarrow.
    # This should be kept larger than actual average inflation multipliers.
    # Note that this is a very rough guess since actual observed pyarrow
    # inflation multiplier for snappy-compressed parquet is about 5.45X for
    # all rows, but here we're trying to guess the inflation multipler for just
    # a primary key SHA1 digest and sort key columns (which could be all columns
    # of the table in the worst case, but here we're assuming that they
    # represent no more than ~1/4th of the total table bytes)
    PYARROW_INFLATION_MULTIPLIER = 1.5

    # we assume here that we're running on a fixed-size cluster
    # this assumption could be removed, but we'd still need to know the max
    # resources we COULD get for this cluster, and the amount of memory
    # available per CPU should remain fixed across the cluster.
    worker_cpus = int(cluster_resources["CPU"])
    worker_obj_store_mem = ray_constants.from_memory_units(
        cluster_resources["object_store_memory"]
    )
    logger.info(f"Total worker object store memory: {worker_obj_store_mem}")
    worker_obj_store_mem_per_task = worker_obj_store_mem / worker_cpus
    logger.info(f"Worker object store memory/task: "
                f"{worker_obj_store_mem_per_task}")
    worker_task_mem = ray_constants.from_memory_units(
        cluster_resources["memory"]
    )
    logger.info(f"Total worker memory: {worker_task_mem}")
    # TODO (pdames): ensure fixed memory per CPU in heterogenous clusters
    worker_mem_per_task = worker_task_mem / worker_cpus
    logger.info(f"Cluster worker memory/task: {worker_mem_per_task}")

    delta_bytes = 0
    delta_bytes_pyarrow = 0
    latest_stream_position = -1
    limited_input_da_list = []
    for delta in input_deltas:
        manifest = deltacat_storage.get_delta_manifest(delta)
        dc_delta.set_manifest(delta, manifest)
        # TODO (pdames): ensure pyarrow object fits in per-task obj store mem
        position = dc_delta.get_stream_position(delta)
        manifest_entries = rsm.get_entries(dc_delta.get_manifest(delta))
        for entry in manifest_entries:
            # TODO: Fetch s3_obj["Size"] if entry content length undefined?
            delta_bytes += rsmm.get_content_length(rsme.get_meta(entry))
            delta_bytes_pyarrow = delta_bytes * PYARROW_INFLATION_MULTIPLIER
            latest_stream_position = max(position, latest_stream_position)
        if delta_bytes_pyarrow > worker_obj_store_mem:
            logger.info(
                f"Input deltas limited to "
                f"{len(limited_input_da_list)} by object store mem "
                f"({delta_bytes_pyarrow} > {worker_obj_store_mem})")
            break
        delta_annotated = da.from_delta(delta)
        limited_input_da_list.append(delta_annotated)

    logger.info(f"Input deltas to compact this round: "
                f"{len(limited_input_da_list)}")
    logger.info(f"Input delta bytes to compact: {delta_bytes}")
    logger.info(f"Latest input delta stream position: {latest_stream_position}")

    if not limited_input_da_list:
        raise RuntimeError("No input deltas to compact!")

    # TODO (pdames): determine min hash buckets from size of all deltas
    #  (not just deltas for this round)
    min_hash_bucket_count = math.ceil(
        delta_bytes_pyarrow / worker_obj_store_mem_per_task
    )
    logger.info(f"Minimum recommended hash buckets: {min_hash_bucket_count}")

    if hash_bucket_count is None:
        # TODO (pdames): calc default hash buckets from table growth rate... as
        #  this stands, we don't know whether we're provisioning insufficient
        #  hash buckets for the next 5 minutes of deltas or more than enough
        #  for the next 10 years
        hash_bucket_count = min_hash_bucket_count
        logger.info(f"Using default hash bucket count: {hash_bucket_count}")

    if hash_bucket_count < min_hash_bucket_count:
        logger.warning(
            f"Provided hash bucket count ({hash_bucket_count}) "
            f"is less than the min recommended ({min_hash_bucket_count}). "
            f"This compaction job run may run out of memory. To resolve this "
            f"problem either specify a larger number of hash buckets when "
            f"running compaction, omit a custom hash bucket count when "
            f"running compaction, or provision workers with more task "
            f"memory per CPU.")

    hash_bucket_chunk_size = user_hash_bucket_chunk_size
    max_hash_bucket_chunk_size = math.ceil(
        worker_obj_store_mem_per_task / PYARROW_INFLATION_MULTIPLIER
    )
    logger.info(f"Max hash bucket chunk size: {max_hash_bucket_chunk_size}")
    if hash_bucket_chunk_size > max_hash_bucket_chunk_size:
        # TODO (pdames): note type of memory to increase (task or object store)
        logger.warning(
            f"Provided hash bucket chunk size "
            f"({user_hash_bucket_chunk_size}) is greater than the max "
            f"recommended ({max_hash_bucket_chunk_size}). This compaction "
            f"job may run out of memory. To resolve this problem either "
            f"specify a smaller hash bucket chunk size when running "
            f"compaction, omit a custom hash bucket chunk size when running "
            f"compaction, or provision workers with more task and object "
            f"store memory per CPU.")
    elif not hash_bucket_chunk_size:
        hash_bucket_chunk_size = math.ceil(max_hash_bucket_chunk_size)
        logger.info(f"Default hash bucket chunk size: {hash_bucket_chunk_size}")

    rebatched_da_list = da.rebatch(
        limited_input_da_list,
        hash_bucket_chunk_size,
    )

    logger.info(f"Hash bucket chunk size: {hash_bucket_chunk_size}")
    logger.info(f"Hash bucket count: {hash_bucket_count}")
    logger.info(f"Input uniform delta count: {len(rebatched_da_list)}")

    return rebatched_da_list, hash_bucket_count, latest_stream_position
