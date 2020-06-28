"""
Given a list of numbers, compute their sum.

Changes data generation method for sum.py for different results
"""
import pandas as pd
from numba import jit
import numpy as np
import random

from typing import List

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

def random_numeric_list_v2(n: int) -> List[float]:
    return [random.random() for _ in range(n)]


@time_this(lambda x: len(x))
def fast_sum(values: List[float]) -> float:
    accum = 0
    for value in values:
        accum += value
    return value

@time_this(lambda x: len(x))
def fast_native_sum(values: List[float]) -> float:
    return sum(values)

@time_this(lambda x: len(x))
def numpy_fast_sum(values: np.ndarray) -> float:
    return np.sum(values)

@time_this(lambda x: len(x))
def pandas_fast_sum(values: pd.Series) -> float:
    return values.sum()

@jit(nopython=True)
def _numba_fast_sum(values: np.ndarray) -> float:
    """
    JIT compilation occurs after one use
    """
    accum = 0
    for value in values:
        accum += value
    return accum

# Force numba to run jit compilation
_numba_fast_sum(np.array(random_numeric_list_v2(100000)))


@time_this(lambda x: len(x))
def numba_fast_sum(values: np.ndarray) -> float:
    """
    Redeclare optimized wrapper
    """
    return _numba_fast_sum(values)

if __name__ == '__main__':

    exp_range = ExponentialRange(0, 8, 1/4)
    values = random_numeric_list_v2(exp_range.max)

    with timed_report():
        for i in exp_range.iterator():
            fast_sum(values[:i])

        for i in exp_range.iterator():
            fast_native_sum(values[:i])

        for i in exp_range.iterator():
            numpy_fast_sum(np.array(values[:i]))

        for i in exp_range.iterator():
            pandas_fast_sum(pd.Series(values[:i]))

        for i in exp_range.iterator():
            numba_fast_sum(np.array(values[:i]))

