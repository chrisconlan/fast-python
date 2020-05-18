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

from typing import List, Tuple, Dict

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

def random_words(n: int) -> List[str]:
    characters = string.ascii_uppercase + string.digits
    big_list = random.choices(characters, k=n*7)
    return [''.join(big_list[i:(i+7)]) for i in range(n)]

def random_characters(n: int) -> List[str]:
    characters = string.ascii_uppercase + string.digits
    return random.choices(characters, k=n)

@time_this(lambda *args, **kwargs: len(args[0]))
def slow_count_occurrences(
    the_words: List[str]) -> List[Tuple[str, int]]:
    """
    This algorithm is O(nm) for n total words and m unique 
    words
    """

    # Our output data structure will be a list of tuples
    count_by_word = list()

    # Get a list of all unique words using set
    unique_words = set(the_words)

    # Loop through unique words
    for word_a in unique_words:

        # Count the occurences
        accumulator = 0
        for word_b in the_words:
            if word_a == word_b:
                accumulator += 1

        # Store the character with the count
        count_by_word.append((word_a, accumulator))

    return count_by_word


@time_this(lambda *args, **kwargs: len(args[0]))
def fast_count_occurrences(
    the_words: List[str]) -> Dict[str, int]:
    """
    This algorithm is O(n) for n words
    """

    # Our output data structure
    count_by_word = dict()

    # Loop through the words
    for word in the_words:

        # Make sure the dictionary knows about the words
        if not word in count_by_word:
            count_by_word[word] = 0

        # Incriment the counter
        count_by_word[word] += 1

    return count_by_word


@time_this(lambda *args, **kwargs: len(args[0]))
def defaultdict_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    """
    This algorithm is O(n) for n words
    """

    # A dictionary whose values default to zero
    count_by_word = defaultdict(int)

    # Loop through the words
    for word in the_words:

        # Incriment the counter
        count_by_word[word] += 1

    return count_by_word


@time_this(lambda *args, **kwargs: len(args[0]))
def counter_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    """
    This algorithm is O(n) for n words
    """
    return Counter(the_words)


@time_this(lambda *args, **kwargs: len(args[0]))
def np_fast_count(
    the_words: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    This algorithm is O(n) for n words
    """
    return np.unique(the_words, return_counts=True)

@time_this(lambda *args, **kwargs: len(args[0]))
def pd_fast_count(
    the_words: pd.Series) -> pd.Series:
    """
    This algorithm is O(n) for n words
    """
    return the_words.value_counts()


from collections import Counter
from joblib import Parallel, delayed
import math

def _counter_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    return Counter(the_words)

N_JOBS = 8

@time_this(lambda *args, **kwargs: len(args[0]))
def parallel_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    """
    Count words in parallel using joblib, then aggregate the
    results. This is still O(n+m) complexity for constant k,
    or O(n+km) for variable k.
    """

    # Figure out chunk sizes
    s = chunk_size = math.ceil(len(the_words) / N_JOBS)
    chunk_slices = [(i*s, (i+1)*s) for i in range(N_JOBS)]

    # Set up parallel wrapper and functions
    parallel = Parallel(n_jobs=N_JOBS)
    delayed_count = delayed(_counter_fast_count)
    
    # Dispatch parallel computation
    counters: List[Dict[str, int]] = parallel(
        delayed_count(the_words[i:j]) for \
        i, j in chunk_slices
    )

    # Aggregate result
    result_count: Dict[str, int] = Counter()
    for counter in counters:
        # Counter.update sums counts
        result_count.update(counter)

    return result_count

if __name__ == '__main__':

    # the_words = ['A', 'A', 'A', 'B', 'B', 'B', 'C'] * 100
    # print(slow_count_occurrences(the_words))
    # print(fast_count_occurrences(the_words))
    # print(defaultdict_fast_count(the_words))
    # print(counter_fast_count(the_words))
    # print(np_fast_count(np.array(the_words)))
    # print(pd_fast_count(pd.Series(the_words)))
    # print(parallel_fast_count(the_words))

    exp_range = ExponentialRange(0, 7, 1/4)
    the_words = random_words(exp_range.max)
    the_array = np.array(the_words)
    the_series = pd.Series(the_words)

    with timed_report():
        for i in exp_range.iterator(4):
            slow_count_occurrences(the_words[:i])

        for i in exp_range.iterator():
            fast_count_occurrences(the_words[:i])

        for i in exp_range.iterator():
            defaultdict_fast_count(the_words[:i])

        for i in exp_range.iterator():
            counter_fast_count(the_words[:i])

        for i in exp_range.iterator():
            np_fast_count(the_array[:i])

        for i in exp_range.iterator():
            pd_fast_count(the_series[:i])

        for i in exp_range.iterator():
            parallel_fast_count(the_words[:i])

    exp_range = ExponentialRange(2, 8, 1/4)
    the_words = random_characters(exp_range.max)
    the_array = np.array(the_words)
    the_series = pd.Series(the_words)
    
    with timed_report():
        for i in exp_range.iterator(6):
            slow_count_occurrences(the_words[:i])

        for i in exp_range.iterator():
            fast_count_occurrences(the_words[:i])

        for i in exp_range.iterator():
            defaultdict_fast_count(the_words[:i])

        for i in exp_range.iterator():
            counter_fast_count(the_words[:i])

        for i in exp_range.iterator():
            np_fast_count(the_array[:i])

        for i in exp_range.iterator(6):
            pd_fast_count(the_series[:i])

        for i in exp_range.iterator(7):
            if i < 100:
                continue
            parallel_fast_count(the_words[:i])
