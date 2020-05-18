"""
Given a list of words, count the number of occurrences of 
each word in the list. Return a logical data structure to 
represent the count corresponding to each word.
"""
import random
import string
import pandas as pd
import numpy as np
from numba import jit
from collections import defaultdict, Counter
import re
import os

from typing import List, Tuple, Dict

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

src_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(src_dir, '..', 'data')
fpath = os.path.join(data_dir, 'complete_shakespeare.txt')

shakespeare_chars = 5573152

def read_shakespeare():
    with open(fpath, 'r') as file_ptr:
        data = file_ptr.read()
    return data.lower()

@time_this(lambda *args, **kwargs: shakespeare_chars)
def str_split_count(data: str, value: str) -> int:
    """
    Return the number of occurrences of value in data by 
    splitting data along value into a list
    """
    return len(data.split(value)) - 1

@time_this(lambda *args, **kwargs: shakespeare_chars)
def str_count(data: str, value: str) -> int:
    """
    Simply call python's str.count method
    """
    return data.count(value)

@time_this(lambda *args, **kwargs: shakespeare_chars)
def re_subn_count(data: str, value: str) -> int:
    """
    Count the number of substitutions that value word 
    perform on data in a regex substitution
    """
    return re.subn(value, '', data)[1]

@time_this(lambda *args, **kwargs: shakespeare_chars)
def re_findall_count(data: str, value: str) -> int:
    """
    Count the number of elements returned in an exhaustive 
    regex search of value on data
    """
    return len(re.findall(value, data))

@time_this(lambda *args, **kwargs: shakespeare_chars)
def re_finditer_count(data: str, value: str) -> int:
    """
    Count the number of elements returned in an exhaustive 
    regex search of value on data, as an iterator
    """
    return sum(1 for _ in re.finditer(value, data))


from collections import Counter

def counter_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    """
    This algorithm is O(n) for n words
    """
    return Counter(the_words)



if __name__ == '__main__':
    data = read_shakespeare()
    print(len(data))

    # counter = counter_fast_count(data.split())
    # _counter = [(k,v) for k,v in counter.items()]
    # _counter.sort(key=lambda x: x[1], reverse=True)
    # print(json.dumps(_counter[:10]))

    with timed_report():

        print(str_split_count(data, 'juliet'))
        print(str_count(data, 'juliet'))
        print(re_subn_count(data, 'juliet'))
        print(re_findall_count(data, 'juliet'))
        print(re_finditer_count(data, 'juliet'))

    with timed_report():

        print(str_split_count(data, 'the'))
        print(str_count(data, 'the'))
        print(re_subn_count(data, 'the'))
        print(re_findall_count(data, 'the'))
        print(re_finditer_count(data, 'the'))




