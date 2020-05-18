"""
Given a list of numbers, sort it, but only use C-level 
algos
"""
import random
import string
import numpy as np
import pandas as pd
from typing import List, Tuple, Set, Dict

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

import os
src_dir = os.path.basename(os.path.abspath(__file__))
data_dir = os.path.join('..', 'data')
data_path = os.path.join(data_dir, 'contour_plot.png')

def random_numeric_list(n: int) -> List[float]:
    return list(np.random.random(n))

def image_as_one_dimensional_array():
    from PIL import Image
    img = Image.open(data_path)
    img_array = np.asarray(img, dtype=np.uint8)
    return img_array.reshape(-1)

@time_this(lambda *args, **kwargs: len(args[0]))
def python_timsort(values: List[float]):
    values.sort()

@time_this(lambda *args, **kwargs: len(args[0]))
def numpy_timsort(values: List[float]):
    return np.sort(values, kind='stable')

@time_this(lambda *args, **kwargs: len(args[0]))
def numpy_quicksort(values: List[float]):
    return np.sort(values, kind='quicksort')

@time_this(lambda *args, **kwargs: len(args[0]))
def numpy_heapsort(values: List[float]):
    return np.sort(values, kind='heapsort')

def assert_sorted(values):
    n = len(values)
    is_sorted = all(
        values[i] <= values[i+1] for i in range(n-1)
    )
    assert is_sorted, 'values are not sorted.'


def pd_faster_moving_avg(values: pd.Series,
    m: int=20) -> pd.Series:
    """
    This is O(n) time an outperforms the .rolling variant
    """
    cumsum = values.cumsum()
    return (cumsum - cumsum.shift(m)) / m



if __name__ == '__main__':
    exp_range = ExponentialRange(0, 7, 1/4)
    values = random_numeric_list(exp_range.max)
    np_values = np.array(values)

    with timed_report():
        for i in exp_range.iterator(7):
            _values = values[:i].copy()
            python_timsort(_values)
            assert_sorted(_values)

        for i in exp_range.iterator(7):
            _values = numpy_timsort(values[:i])
            assert_sorted(_values)

        for i in exp_range.iterator(7):
            _values = numpy_quicksort(values[:i])
            assert_sorted(_values)

        for i in exp_range.iterator(7):
            _values = numpy_heapsort(values[:i])
            assert_sorted(_values)


    exp_range = ExponentialRange(0, 7, 1/4)
    values = image_as_one_dimensional_array()
    np_values = np.array(values)

    with timed_report():
        for i in exp_range.iterator():
            _values = values[:i].copy()
            python_timsort(_values)
            assert_sorted(_values)

        for i in exp_range.iterator():
            _values = numpy_timsort(values[:i])
            assert_sorted(_values)

        for i in exp_range.iterator():
            _values = numpy_quicksort(values[:i])
            assert_sorted(_values)

        for i in exp_range.iterator():
            _values = numpy_heapsort(values[:i])
            assert_sorted(_values)
            


