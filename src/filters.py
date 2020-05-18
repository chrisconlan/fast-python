"""
Given a list of numbers, convolve it by an arbitrary 
weighting vector defined by a list of weights and an 
offset
"""
import pandas as pd
from numba import jit
import numpy as np

from typing import List, Dict, Set

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

def random_numeric_list(n: int) -> List[float]:
    return list(np.random.random(n))

@time_this(lambda *args, **kwargs: len(args[0]))
def naive_filter(values: List[float], weights: List[float], 
    a: int) -> List[float]:
    """
    This is O(nm) for a list of length n and weights of 
    length m because it makes no assumptions about the 
    shape of the weighting vector
    """

    n, m = len(values), len(weights)
    b = a + m - 1

    # Exit early if m greater than length of values
    if m > n or -a > n or b > n:
        return [None] * len(values)

    # Front and back padding of series
    front_pad = max(-a, 0)
    back_pad = max(b, 0)

    # Apply front pad
    y = [None] * front_pad

    # Compute the filter
    for i in range(front_pad, n - back_pad):
        accumulator = 0
        for j in range(m):
            accumulator += weights[j] * values[i+j+a]
        y.append(accumulator)

    # Apply back pad
    y.extend([None] * back_pad)

    return y


@time_this(lambda *args, **kwargs: len(args[0]))
def smart_filter(values: List[float], weights: List[float], 
    a: int) -> List[float]:
    """
    This is O(nm) for a list of length n and weights of 
    length m. Takes advantage of duplicate weights to save 
    calculations.
    """

    n, m = len(values), len(weights)
    b = a + m - 1

    # Exit early if m greater than length of values
    if m > n or -a > n or b > n:
        return [None] * len(values)

    # Front and back padding of series
    front_pad = max(-a, 0)
    back_pad = max(b, 0)

    # Pre-compute scaled values for each unique weight
    unique_weights: Set[float] = set(weights)
    scaled_vectors: Dict[float, List[float]] = dict()
    for w in unique_weights:
        scaled_vectors[w] = [w * v for v in values]

    # Apply front pad
    y = [None] * front_pad

    # Compute the moving average
    for i in range(front_pad, n - back_pad):
        accumulator = 0
        for j, w in enumerate(weights):
            accumulator += scaled_vectors[w][i+j+a]
        y.append(accumulator)

    # Apply back pad
    y.extend([None] * back_pad)

    return y


@time_this(lambda *args, **kwargs: len(args[0]))
def numpy_naive_filter(values: np.ndarray, 
    weights: np.ndarray, a: int) -> np.ndarray:
    """
    This is O(nm) for a list of length n and weights of 
    length m because it makes no assumptions about the 
    shape of the weighting vector
    """

    n, m = values.shape[0], weights.shape[0]
    b = a + m - 1

    # Exit early if m greater than length of values
    if m > n or -a > n or b > n:
        return np.array([np.nan]*n)

    # Front and back padding of series
    front_pad = max(-a, 0)
    back_pad = max(b, 0)

    # Initialize the output array
    y = np.empty((n,))

    # Pad with na values
    y[:front_pad] = np.nan
    y[-back_pad:] = np.nan

    # Compute the filter
    for i in range(front_pad, n - back_pad):
        y[i] = weights.dot(values[(i+a):(i+a+m)])

    return y

@time_this(lambda *args, **kwargs: len(args[0]))
def numpy_smart_filter(values: np.ndarray, 
    weights: np.ndarray, a: int) -> np.ndarray:
    """
    This is O(nm) for a list of length n and weights of 
    length m. Takes advantage of duplicate weights to save 
    calculations.
    """

    n, m = values.shape[0], weights.shape[0]
    b = a + m - 1

    # Exit early if m greater than length of values
    if m > n or -a > n or b > n:
        return np.array([np.nan]*n)

    # Front and back padding of series
    front_pad = max(-a, 0)
    back_pad = max(b, 0)

    # Initialize the output array
    y = np.zeros((n,))

    # Pad with na values
    y[:front_pad] = np.nan
    y[-back_pad:] = np.nan

    unique_weights: Set[float] = set(weights)
    scaled_vectors: Dict[float, np.ndarray] = dict()
    for w in unique_weights:
        scaled_vectors[w] = w * values

    r1, r2 = front_pad, n-back_pad
    for j, w in enumerate(weights):
        v = scaled_vectors[w]
        y[r1:r2] += v[(r1+j+a):(r2+a+j)]

    return y

@time_this(lambda *args, **kwargs: len(args[0]))
def numpy_naive_matrix_filter(values: np.ndarray, 
    weights: np.ndarray, a: int) -> np.ndarray:
    """
    This is O(nm) for a list of length n and weights of 
    length m. Takes advantage of duplicate weights to save 
    calculations.
    """

    n, m = values.shape[0], weights.shape[0]
    b = a + m - 1

    # Exit early if m greater than length of values
    if m > n or -a > n or b > n:
        return np.array([np.nan]*n)

    # Front and back padding of series
    front_pad = max(-a, 0)
    back_pad = max(b, 0)

    # Initialize the output array
    y = np.zeros((n,))

    # Pad with na values
    y[:front_pad] = np.nan
    y[-back_pad:] = np.nan

    # Build a matrix to multiply with weight vector
    q = np.empty((n - front_pad - back_pad, m))
    for j in range(m):
        q[:,j] = values[j:(j+n-m+1)]

    y[front_pad:-back_pad] = q.dot(weights)

    return y

if __name__ == '__main__':

    exp_range = ExponentialRange(2, 7, 1/4)
    values = random_numeric_list(exp_range.max)
    series_values = pd.Series(values)
    np_values = np.array(values)

    # _values = [1,2,3,4,5,6,7,8,9,10]
    # _weights = [1,2,3,2,1]
    # _a = -2
    # print(naive_filter(_values, _weights, _a))
    # print(smart_filter(_values, _weights, _a))
    # print(
    #     numpy_naive_filter(
    #         np.array(_values), 
    #         np.array(_weights), 
    #         _a,
    #     )
    # )
    # print(
    #     numpy_smart_filter(
    #         np.array(_values), 
    #         np.array(_weights), 
    #         _a,
    #     )
    # )

    # print(
    #     numpy_naive_matrix_filter(
    #         np.array(_values), 
    #         np.array(_weights), 
    #         _a,
    #     )
    # )

    m = 21
    weights = [1/m]*m
    np_weights = np.array(weights)
    a = -int((m-1)/2)

    with timed_report():
        for i in exp_range.iterator(6):
            naive_filter(values[:i], weights, a)

        for i in exp_range.iterator(6):
            smart_filter(values[:i], weights, a)

        for i in exp_range.iterator():
            numpy_naive_filter(np_values[:i], np_weights, a)

        for i in exp_range.iterator():
            numpy_smart_filter(np_values[:i], np_weights, a)

        for i in exp_range.iterator():
            numpy_naive_matrix_filter(np_values[:i], np_weights, a)
           

    m = 21
    weights = list(np.random.random(m))
    np_weights = np.array(weights)
    a = -int((m-1)/2)

    with timed_report():
        for i in exp_range.iterator(6):
            naive_filter(values[:i], weights, a)

        for i in exp_range.iterator(6):
            smart_filter(values[:i], weights, a)

        for i in exp_range.iterator():
            numpy_naive_filter(np_values[:i], np_weights, a)

        for i in exp_range.iterator():
            numpy_smart_filter(np_values[:i], np_weights, a)

        for i in exp_range.iterator():
            numpy_naive_matrix_filter(np_values[:i], np_weights, a)


