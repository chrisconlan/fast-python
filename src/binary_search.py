"""
Given a sorted list of numbers, determine if an element is 
in a list
"""
import random
import string
import numpy as np
import pandas as pd
from typing import List, Tuple, Set, Dict

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

import bisect

def random_numeric_list(n: int) -> List[float]:
    return list(np.random.random(n))

@time_this(lambda *args, **kwargs: len(args[0]))
def naive_in_operator(values: List[float], 
    target: float) -> bool:
    """
    Given a list of floats that are assumed to be sorted, 
    determine if an element is in the list with early 
    stopping. This is O(n)
    """
    for value in values:
        if target == value:
            return True

def _binary_search_in(values: np.ndarray, 
    target: float) -> bool:
    """
    Recursive part of binary_search_in
    """

    # Split list in half
    n = len(values)
    i = n // 2
        
    if n > 1: 
        # Search the upper or lower part of the list
        if target >= values[i]:
            return _binary_search_in(values[i:], target)
        else:
            return _binary_search_in(values[:i], target)
    else:
        # Else, test for equality
        return values[i] == target

@time_this(lambda *args, **kwargs: len(args[0]))
def binary_search_in(values: np.ndarray, 
    target: float) -> bool:
    """
    Given a numpy array of floats that are assumed to be 
    sorted, determine if an element is in it. We use numpy 
    arrays here because it is important that array slices 
    are passed by reference, rather than copied.
    This is O(log(n))
    """
    return _binary_search_in(values, target)

@time_this(lambda *args, **kwargs: len(args[0]))
def bisect_search_in(values: List[float], 
    target: float) -> bool:
    """
    Given a list of floats that are assumed to be sorted, 
    determine if an element is in the list using Python's 
    bisect library. This is O(log(n))
    """

    # Find the insertion point of target within values to 
    # maintain search order using binary search
    i = bisect.bisect_left(values, target)

    # If in bounds, make comparison
    if 0 <= i < len(values):
        return values[i] == target

    # Otherwise it is definitely not a match
    return False



if __name__ == '__main__':

    exp_range = ExponentialRange(1, 7, 1/4)
    values = random_numeric_list(exp_range.max)
    values.sort()

    with timed_report():
        for i in exp_range.iterator():
            result = naive_in_operator(values[:i], values[i-1])
            assert  result

        for i in exp_range.iterator():
            result = binary_search_in(np.array(values[:i]), values[i-1])
            assert  result

        for i in exp_range.iterator():
            result = bisect_search_in(values[:i], values[i-1])
            assert  result
