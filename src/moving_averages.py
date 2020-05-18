"""
Given a list of numbers, compute their moving average
Output the cumulative sum to a new sequence
"""
import pandas as pd
from numba import jit
import numpy as np

from typing import List

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

import gc

def random_numeric_list(n: int) -> List[float]:
    return list(np.random.random(n))

@time_this(lambda *args, **kwargs: len(args[0]))
def slow_moving_avg(values: List[float], 
    m: int=20) -> List[float]:
    """
    This is O(nm) for a list of length n because it 
    re-computes the average at each step
    """

    # Exit early if m greater than length of values
    if m > len(values):
        return [None] * len(values)

    # Pad initial m-1 values with Nones
    moving_avg = [None] * (m-1)

    # Compute the moving average
    for i in range(m-1, len(values)):
        the_avg = sum(values[(i-m+1):(i+1)]) / m
        moving_avg.append(the_avg)

    return moving_avg


@time_this(lambda *args, **kwargs: len(args[0]))
def fast_moving_avg(values: List[float], 
    m: int=20) -> List[float]:
    """
    This is O(n) for a list of length n because it 
    uses the differential of the accumulator at each step
    """

    # Exit early if m greater than length of values
    if m > len(values):
        return [None] * len(values)

    # Pad initial m-1 values with Nones
    moving_avg = [None] * (m-1)

    # Compute the initial values
    accumulator = sum(values[:m])
    moving_avg.append(accumulator / m)

    # Loop through the remainder of the data
    for i in range(m, len(values)):

        # Subtract the out-of-window value
        accumulator -= values[i-m]

        # Add the new in-window value
        accumulator += values[i]

        # Store the average
        moving_avg.append(accumulator / m)

    return moving_avg


@time_this(lambda *args, **kwargs: len(args[0]))
def np_fast_moving_avg(values: np.ndarray, 
    m: int=20) -> np.ndarray:
    """
    Calculate the moving average in numpy in O(n) time. 
    Calculate v_i in advance using lagged difference of the 
    cumsum.
    """

    # Calculate the cumulative sum to derive v_i from
    cumsum = np.cumsum(values)

    # Initialize empty array
    moving_avg = np.empty((len(values),))

    # Fill it with results
    moving_avg[:m-1] = np.nan

    if m <= values.shape[0]:
        moving_avg[m-1] = cumsum[m-1] / m

    if m < values.shape[0]:
        moving_avg[m:] = (cumsum[m:] - cumsum[:-m]) / m

    return moving_avg
    
@time_this(lambda *args, **kwargs: len(args[0]))
def pd_fast_moving_avg(values: pd.Series,
    m: int=20) -> pd.Series:
    """
    This is O(n) time and utilizes pandas .rolling interface
    """
    return values.rolling(m).mean()

@time_this(lambda *args, **kwargs: len(args[0]))
def pd_faster_moving_avg(values: pd.Series,
    m: int=20) -> pd.Series:
    """
    This is O(n) time an outperforms the .rolling variant
    """
    cumsum = values.cumsum()
    return (cumsum - cumsum.shift(m)) / m


@jit(nopython=True)
def _numba_fast_moving_avg(values: np.ndarray, 
    m: int=20) -> np.ndarray:
    """
    This is O(n) time and just-in-time compiled with numba
    """

    # Initialize arrays to store data
    moving_avg = np.empty(values.shape)
    moving_avg[:m-1] = np.nan

    # Exit early if m greater than length of values
    if m > values.shape[0]:
        return moving_avg

    # Compute the initial values
    accumulator = np.sum(values[:m])
    moving_avg[m-1] = accumulator / m

    # Loop through the remainder of the data
    for i in range(m, values.shape[0]):

        # Subtract the out-of-window value
        accumulator -= values[i-m]

        # Add the new in-window value
        accumulator += values[i]

        # Store the average
        moving_avg[i] = accumulator / m

    return moving_avg

# Get numba to run the jit optimization
_numba_fast_moving_avg(np.random.random(100000))

# Register time-able version of function
@time_this(lambda *args, **kwargs: len(args[0]))
def numba_fast_moving_avg(values: np.ndarray, 
    m: int=20) -> np.ndarray:
    return _numba_fast_moving_avg(values, m=m)

if __name__ == '__main__':

    exp_range = ExponentialRange(2, 7, 1/4)
    values = random_numeric_list(exp_range.max)
    series_values = pd.Series(values)
    np_values = np.array(values)

    with timed_report():
        for i in exp_range.iterator(5):
            slow_moving_avg(values[:i], m=100)
            gc.collect()

        for i in exp_range.iterator(7):
            fast_moving_avg(values[:i], m=100)
            gc.collect()

        for i in exp_range.iterator():
            np_fast_moving_avg(np_values[:i], m=100)
            gc.collect()

        for i in exp_range.iterator():
            pd_fast_moving_avg(series_values[:i], m=100)
            gc.collect()

        for i in exp_range.iterator():
            pd_faster_moving_avg(series_values[:i], m=100)
            gc.collect()

        for i in exp_range.iterator():
            numba_fast_moving_avg(np_values[:i], m=100)
            gc.collect()
