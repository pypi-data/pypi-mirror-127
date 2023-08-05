from typing import Dict, Callable, Type, Union

import numpy as np
import pandas as pd
import pyarrow as pa

from ray.data.dataset import Dataset

from deltacat.types.media import TableType
from deltacat.utils import pyarrow as pa_utils, pandas as pd_utils, \
    numpy as np_utils
from deltacat.utils.ray_utils import dataset as ds_utils
from deltacat.storage.interface import LocalTable, DistributedDataset

TABLE_TYPE_TO_READER_FUNC: Dict[int, Callable] = {
    TableType.PYARROW.value: pa_utils.s3_file_to_table,
    TableType.PANDAS.value: pd_utils.s3_file_to_dataframe,
    TableType.NUMPY.value: np_utils.s3_file_to_ndarray
}

TABLE_CLASS_TO_WRITER_FUNC: Dict[
    Type[Union[LocalTable, DistributedDataset]], Callable] = {
    pa.Table: pa_utils.table_to_file,
    pd.DataFrame: pd_utils.dataframe_to_file,
    np.ndarray: np_utils.ndarray_to_file,
    Dataset: ds_utils.dataset_to_file,
}

TABLE_CLASS_TO_SLICER_FUNC: Dict[
    Type[Union[LocalTable, DistributedDataset]], Callable] = {
    pa.Table: pa_utils.slice_table,
    pd.DataFrame: pd_utils.slice_dataframe,
    np.ndarray: np_utils.slice_ndarray,
    Dataset: ds_utils.slice_dataset,
}

TABLE_CLASS_TO_SIZE_FUNC: Dict[
    Type[Union[LocalTable, DistributedDataset]], Callable] = {
    pa.Table: pa_utils.table_size,
    pd.DataFrame: pd_utils.dataframe_size,
    np.ndarray: np_utils.ndarray_size,
    Dataset: ds_utils.dataset_size,
}


def get_table_length(table: Union[LocalTable, DistributedDataset]) -> int:
    return len(table) if not isinstance(table, Dataset) else table.count()


def get_table_writer(table: Union[LocalTable, DistributedDataset]) \
        -> Callable:

    table_writer_func = TABLE_CLASS_TO_WRITER_FUNC.get(type(table))
    if table_writer_func is None:
        msg = f"No writer found for table type: {type(table)}.\n" \
              f"Known table types: {TABLE_CLASS_TO_WRITER_FUNC.keys}"
        raise ValueError(msg)
    return table_writer_func


def get_table_slicer(table: Union[LocalTable, DistributedDataset]) -> Callable:
    table_slicer_func = TABLE_CLASS_TO_SLICER_FUNC.get(type(table))
    if table_slicer_func is None:
        msg = f"No slicer found for table type: {type(table)}.\n" \
              f"Known table types: {TABLE_CLASS_TO_SLICER_FUNC.keys}"
        raise ValueError(msg)
    return table_slicer_func
