"""
Given a list of numbers, compute their cumulative sum
Output the cumulative sum to a new sequence
"""
import pandas as pd
from numba import jit
import numpy as np

from typing import List

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

def random_numeric_list(n: int) -> List[float]:
    return list(np.random.random(n))

@time_this(lambda x: len(x))
def slow_cusum(values: List[float]) -> List[float]:
    """
    This is O(n^2) time, because it computes ...
    1
    1 + 2
    1 + 2 + 3
    1 + 2 + 3 + 4
    and so on ...
    Leading to n*(n-1)/2 individual additions, 
    which is O(n^2)
    """
    cusum = []

    for i in range(len(values)):
        the_sum = sum(values[:i+1])
        cusum.append(the_sum)

    return cusum

@time_this(lambda x: len(x))
def slow_cusum_expanded(values: List[float]) -> List[float]:
    """
    Same as the above, O(n^2), but exposes the hidden 
    complexity of sum()
    """
    cusum = []

    for i in range(len(values)):

        accumulator = 0
        for j in range(i+1):
            accumulator += values[j]

        cusum.append(accumulator)

    return cusum

@time_this(lambda x: len(x))
def python_fast_cusum(values: List[float]) -> List[float]:
    """
    This is O(n) time, because it does n additions for n 
    values
    """
    cusum = []
    accumulator = 0

    for value in values:
        accumulator += value
        cusum.append(accumulator)

    return cusum


@time_this(lambda x: len(x))
def pandas_fast_cusum(values: pd.Series) -> pd.Series:
    """
    This is O(n) and optimized with C code
    """
    return values.cumsum()


@jit(nopython=True)
def _numba_fast_cusum(values: np.ndarray) -> np.ndarray:
    """
    This is O(n) time and just-in-time compiled with numba
    """
    cusum = np.zeros(values.shape[0])
    accumulator = 0

    for index, value in enumerate(values):
        accumulator += value
        cusum[index] = accumulator

    return cusum

# Get numba to run the jit optimization
_numba_fast_cusum(np.array(random_numeric_list(10000)))

# Register time-able version of function
@time_this(lambda x: len(x))
def numba_fast_cusum(values: np.ndarray) -> np.ndarray:
    return _numba_fast_cusum(values)


@time_this(lambda x: len(x))
def np_fast_cusum(values: np.ndarray) -> np.ndarray:
    """
    This is O(n) and optimized with C code
    """
    return values.cumsum()


if __name__ == '__main__':

    exp_range = ExponentialRange(0, 8, 1/4)
    values = random_numeric_list(exp_range.max)

    with timed_report():
        for i in exp_range.iterator(4):
            slow_cusum(values[:i])

        for i in exp_range.iterator(4):
            slow_cusum_expanded(values[:i])

        for i in exp_range.iterator():
            python_fast_cusum(values[:i])

        for i in exp_range.iterator():
            pandas_fast_cusum(pd.Series(values[:i]))
        
        for i in exp_range.iterator():
            numba_fast_cusum(np.array(values[:i]))

        for i in exp_range.iterator():
            np_fast_cusum(np.array(values[:i]))

