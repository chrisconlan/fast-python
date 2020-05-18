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
def slow_concatenate_words(the_words: List[str]) -> str:
    """
    Concatenate a list of string. This has O(mn^2) memory 
    complexity for n words with an average length of m.
    """
    result: str = ''
    for word in the_words:
        result += word

    return result


@time_this(lambda *args, **kwargs: len(args[0]))
def fast_concatenate_words(the_words: List[str]) -> str:
    """
    Concatenate a list of string. This has O(mn) memory 
    complexity for n words with an average length of m.
    """
    return ''.join(the_words)


if __name__ == '__main__':
    exp_range = ExponentialRange(0, 7, 1/4)
    the_words = random_words(exp_range.max)
    # the_array = np.array(the_words)
    # the_series = pd.Series(the_words)

    with timed_report():
        for i in exp_range.iterator():
            slow_concatenate_words(the_words[:i])

        for i in exp_range.iterator():
            fast_concatenate_words(the_words[:i])
