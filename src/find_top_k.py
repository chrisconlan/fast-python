"""
Given a list of numbers, find the top k elements
"""
import random
import string
import numpy as np
import pandas as pd
from typing import List, Tuple, Set, Dict
import heapq

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

def random_numeric_list(n: int) -> List[float]:
    return list(np.random.random(n))


@time_this(lambda *args, **kwargs: len(args[0]))
def naive_find_top_k(values: List[float], 
    k: int=20) -> List[float]:
    """
    Given a list of values, find the highest k values by 
    sorting the entire list first. This is O(n*log(n))
    """
    values.sort(reverse=True)
    return values[:k]

@time_this(lambda *args, **kwargs: len(args[0]))
def heap_find_top_k(values: List[float], 
    k: int=20) -> List[float]:
    """
    Given a list of values, convert it into a heap in-place,
    then extract the top k values from the heap. This is 
    O(n + k*log(n))
    """
    return heapq.nlargest(k, values)

@time_this(lambda *args, **kwargs: len(args[0]))
def heap_find_top_k_expanded(values: List[float], 
    k: int=20) -> List[float]:
    """
    Given a list of values, convert it into a heap in-place,
    then extract the  top k values from the heap. This is 
    O(n + k*log(n))
    """
    _heap: List[float] = []
    for v in values:
        heapq.heappush(_heap, -v)

    top_k: List[float] = []
    for i in range(k):
        top_k.append(-heapq.heappop(_heap))

    return top_k

def assert_sorted(values):
    n = len(values)
    is_sorted = all(
        values[i] >= values[i+1] for i in range(n-1)
    )
    assert is_sorted, 'values are not sorted.'

def assert_top_k(top_k_values, values):
    assert_sorted(top_k_values)
    kth_value = top_k_values[-1]
    k = len(top_k_values)
    assert sum(v >= kth_value for v in values) == k, \
        'Something went wrong'

if __name__ == '__main__':

    exp_range = ExponentialRange(2, 7, 1/4)
    values = random_numeric_list(exp_range.max)

    with timed_report():
        for i in exp_range.iterator():
            _values = values[:i].copy()
            _top_k = naive_find_top_k(_values)
            assert_top_k(_top_k, _values)

        for i in exp_range.iterator():
            _values = values[:i].copy()
            _top_k = heap_find_top_k(_values)
            assert_top_k(_top_k, _values)

        for i in exp_range.iterator():
            _values = values[:i].copy()
            _top_k = heap_find_top_k_expanded(_values)
            assert_top_k(_top_k, _values)