"""
Given a list of lists of strings, flatten into a single
list of strings
"""
import random
import string
import numpy as np
import pandas as pd
from typing import List, Tuple, Set, Dict
import heapq

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

def random_lists_of_chars(n: int) -> List[List[str]]:
    characters = string.ascii_uppercase + string.digits
    big_list = random.choices(characters, k=n*7)
    return [big_list[i:(i+7)] for i in range(n)]

def random_lists_of_floats(n: int) -> List[List[float]]:
    return [
        [
            random.random() for _j in range(7)
        ] for _i in range(n)
    ]


@time_this(lambda *args, **kwargs: len(args[0]))
def slow_add_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via list addition. This has 
    O(mn^2) compexity for n lists with average length m
    """
    result: List[str] = []
    for _list in the_lists:
        result = result + _list
    return result

@time_this(lambda *args, **kwargs: len(args[0]))
def add_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via list addition
    """
    result: List[str] = []
    for _list in the_lists:
        result += _list
    return result


@time_this(lambda *args, **kwargs: len(args[0]))
def extend_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via extend
    """
    result: List[str] = []
    for _list in the_lists:
        result.extend(_list)
    return result

@time_this(lambda *args, **kwargs: len(args[0]))
def append_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via nested append
    """
    result: List[str] = []
    for _list in the_lists:
        for val in _list:
            result.append(val)
    return result

@time_this(lambda *args, **kwargs: len(args[0]))
def comprehension_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via nested list comprehension
    """
    return [val for _list in the_lists for val in _list]

if __name__ == '__main__':

    # test_lists = [[1,2,3],[5,6,7],[3,4],[1]]
    # print(slow_add_flatten_lists(test_lists))
    # print(add_flatten_lists(test_lists))
    # print(extend_flatten_lists(test_lists))
    # print(append_flatten_lists(test_lists))
    # print(comprehension_flatten_lists(test_lists))

    exp_range = ExponentialRange(0, 7, 1/4)
    the_lists = random_lists_of_chars(exp_range.max)
    # the_array = np.array(the_words)
    # the_series = pd.Series(the_words)

    with timed_report():
        for i in exp_range.iterator(4):
            slow_add_flatten_lists(the_lists[:i])

        for i in exp_range.iterator():
            add_flatten_lists(the_lists[:i])

        for i in exp_range.iterator():
            extend_flatten_lists(the_lists[:i])

        for i in exp_range.iterator():
            append_flatten_lists(the_lists[:i])

        for i in exp_range.iterator():
            comprehension_flatten_lists(the_lists[:i])
