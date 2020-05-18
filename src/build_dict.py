"""
Given a list of string, concatenate them
"""
import random
import string
import numpy as np
import pandas as pd
from typing import List, Tuple, Set, Dict
import heapq

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange


def random_words(n: int) -> List[str]:
    characters = string.ascii_uppercase + string.digits
    big_list = random.choices(characters, k=n*7)
    return [''.join(big_list[i:(i+7)]) for i in range(n)]
    

@time_this(lambda *args, **kwargs: len(args[0]))
def loop_build_dict(words: List[str]) -> Dict[str, str]:
    """
    Build a dictionary by looping through each element of 
    the list and declaring it as the key-value pair
    """
    result = dict()
    for word in words:
        result[word] = word
    return result


@time_this(lambda *args, **kwargs: len(args[0]))
def list_build_dict(
    words: List[str]) -> Dict[str, str]:
    """
    Build a dictionary by passing a list of tuples to the 
    dict constructor
    """
    return dict([(w, w) for w in words])

@time_this(lambda *args, **kwargs: len(args[0]))
def generator_build_dict(
    words: List[str]) -> Dict[str, str]:
    """
    Build a dictionary by passing a generator of tuples to 
    the dict constructor
    """
    return dict(((w, w) for w in words))

@time_this(lambda *args, **kwargs: len(args[0]))
def comprehension_build_dict(
    words: List[str]) -> Dict[str, str]:
    """
    Build a dictionary using a dict comprehension
    """
    return {w: w for w in words}


if __name__ == '__main__':
    exp_range = ExponentialRange(0, 7, 1/4)
    words = random_words(exp_range.max)

    with timed_report():
        for i in exp_range.iterator():
            loop_build_dict(words[:i])

        for i in exp_range.iterator():
            list_build_dict(words[:i])

        for i in exp_range.iterator():
            generator_build_dict(words[:i])

        for i in exp_range.iterator():
            comprehension_build_dict(words[:i])
