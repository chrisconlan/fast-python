"""
Given a pandas dataframe with unknown dimensions and column
names, loop through it. Stored the last element of the row
in a variable, accessed by its column name.
"""
import pandas as pd
from numba import jit
import numpy as np

from typing import List, Dict, Set, Tuple

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

import random
import itertools
import string

def sample_column_names(n: int, k: int=2) -> List[str]:
    _letters = string.ascii_uppercase
    columns = itertools.product(_letters, repeat=k)
    assert n <= len(_letters)**k, 'Need higher k'
    columns = list(columns)[:n]
    return [''.join(col) for col in columns]

def random_numeric_data_frame(shape: Tuple[int,int]):
	return pd.DataFrame(
		np.random.random(shape),
		columns=sample_column_names(shape[1])
	)


@time_this(lambda x: x.shape[0])
def index_loop_df(df: pd.DataFrame):
    """
    Use the pandas index to look up the row at each step. 
    pandas indexes are dict-like, so the lookup in O(1).
    """
    last_column = df.columns.values[-1]
    for i in df.index:
        row: pd.Series = df.loc[i]
        val = row[last_column]

@time_this(lambda x: x.shape[0])
def iloc_loop_df(df: pd.DataFrame):
    """
    Use the a range-based index to look up the row at each
    step, side-stepping the index. This should skip a 
    hashing operation and be faster than the index lookup.
    """
    last_column = df.columns.values[-1]
    for i in range(df.shape[0]):
        row: pd.Series = df.iloc[i]
        val = row[last_column]

@time_this(lambda x: x.shape[0])
def iterrows_loop_df(df: pd.DataFrame):
    """
    Iterrows is the vanilla and recommended solution for 
    looping through data frames
    """
    last_column = df.columns.values[-1]
    for i, row in df.iterrows():
        # row is a pd.Series
        val = row[last_column]

@time_this(lambda x: x.shape[0])
def itertuples_loop_df(df: pd.DataFrame):
    """
    .itertuples doesn't allow named-based indexing of 
    closures, but it does allow range-based indexing, so 
    we map each column to its range-based position 
    beforehand.
    """
    last_column = df.columns.values[-1]
    col_index_by_name = {
        col: i for i, col in enumerate(df.columns.values)
    }
    for row in df.itertuples():
        # Row is type pd.core.frame.Pandas,
        # which appears to be a private object
        # similar to a collections.namedtuple
        val = row[col_index_by_name[last_column]]

@time_this(lambda x: x.shape[0])
def values_loop_df(df: pd.DataFrame):
    """
    .values converts the data frame to a numpy array before 
    looping, which is fast but no memory-friendly
    """
    last_column = df.columns.values[-1]
    col_index_by_name = {
        col: i for i, col in enumerate(df.columns.values)
    }
    for row in df.values:
        val = row[col_index_by_name[last_column]]

if __name__ == '__main__':

    # df = pd.DataFrame(
    #     [[1,2], [3,4,], [5,6], [7,8]], 
    #     columns=['A', 'B']
    # )
    # index_loop_df(df)
    # iterrows_loop_df(df)
    # itertuples_loop_df(df)
    # values_loop_df(df)

    exp_range = ExponentialRange(0, 5, 1/4)
    df = random_numeric_data_frame((exp_range.max, 500))

    with timed_report():
        for i in exp_range.iterator():
            index_loop_df(df.iloc[:i])

        for i in exp_range.iterator():
            iloc_loop_df(df.iloc[:i])

        for i in exp_range.iterator():
            iterrows_loop_df(df.iloc[:i])

        for i in exp_range.iterator():
            itertuples_loop_df(df.iloc[:i])

        for i in exp_range.iterator():
            values_loop_df(df.iloc[:i])


