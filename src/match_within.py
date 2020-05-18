"""
Given two lists of words, return the elements from the first list that are in 
the second list.
"""
import random
import string
import pandas as pd
from typing import List, Tuple, Set, Dict

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

def random_words(n: int) -> List[str]:
    characters = string.ascii_uppercase + string.digits
    big_list = random.choices(characters, k=n*7)
    return [''.join(big_list[i:(i+7)]) for i in range(n)]

def random_characters(n: int) -> List[str]:
    characters = string.ascii_uppercase + string.digits
    return random.choices(characters, k=n)

@time_this(lambda *args, **kwargs: 2*len(args[0]))
def very_slow_match_within(first_list: List[str], 
    second_list: List[str]) -> Set[str]:
    """
    This algorithm is O(nm) for n total words in the first 
    list and m total words in the second list
    """
    words = set()
    for word in first_list:
        if word in second_list:
            words.add(word)

    return words

@time_this(lambda *args, **kwargs: 2*len(args[0]))
def slow_match_within(first_list: List[str], 
    second_list: List[str]) -> List[str]:
    """
    This algorithm is O(nm) for n unique words in the first 
    list and m total words in the second list
    """

    # Get the unique words
    unique_words = set(first_list)

    words = list()
    for word in unique_words:
        if word in second_list:
            words.append(word)

    return words

@time_this(lambda *args, **kwargs: 2*len(args[0]))
def fast_match_within(first_list: List[str], 
    second_list: List[str]) -> List[str]:
    """
    This algorithm is O(n + m) for n unique words in the 
    first list and m total words in the second list
    """

    # Get the unique words
    first_list_unique_words = set(first_list)
    second_list_unique_words = set(second_list)

    words = list()
    for word in first_list_unique_words:
        if word in second_list_unique_words:
            words.append(word)

    return words

@time_this(lambda *args, **kwargs: 2*len(args[0]))
def fast_intersection(first_list: List[str], 
    second_list: List[str]) -> Set[str]:
    """
    This algorithm is O(n + m) for n words in the first 
    list and m words in the second list.

    This problem boils down to a set intersection.
    """
    return set(first_list) & set(second_list)


@time_this(lambda *args, **kwargs: 2*len(args[0]))
def pd_naive_index_match(first_list: List[str], 
    second_list: List[str]) -> List[str]:
    """
    This algorithm is O(n + m) for n words in the first 
    list and m words in the second list

    This is to show that pandas indexes are dict-like 
    even when the elements are not unique
    """

    # Create a pandas index of of the list as-is
    index: pd.Index = pd.Index(first_list)

    words: List[str] = []
    for word in set(second_list):
        if word in index:
            words.append(word)

    return words


@time_this(lambda *args, **kwargs: 2*len(args[0]))
def pd_unique_index_match(first_list: List[str], 
    second_list: List[str]) -> List[str]:
    """
    This algorithm is O(n + m) for n words in the first 
    list and m words in the second list

    This is to show that pandas indexes are dict-like, 
    and performance increases for unique elements
    """

    # Create a pandas index from unique elements
    index: pd.Index = pd.Index(set(first_list))

    words: List[str] = []
    for word in set(second_list):
        if word in index:
            words.append(word)

    return words


@time_this(lambda *args, **kwargs: 2*len(args[0]))
def pd_native_index_match(first_list: List[str], 
    second_list: List[str]) -> pd.Index:
    """
    This algorithm is O(n + m) for n words in the first 
    list and m words in the second list

    This is to show that pandas indexes are dict-like
    """

    # Create a pandas index from unique elements
    first_index = pd.Index(set(first_list))
    second_index = pd.Index(set(second_list))
    return first_index.intersection(second_index)



if __name__ == '__main__':

    # words_a = ['A', 'B', 'C', 'D']
    # words_b = ['B', 'C', 'D', 'E']

    # print(very_slow_match_within(words_a, words_b))
    # print(slow_match_within(words_a, words_b))
    # print(fast_match_within(words_a, words_b))
    # print(fast_intersection(words_a, words_b))
    # print(pd_unique_index_match(words_a, words_b))
    # print(pd_native_index_match(words_a, words_b))

    exp_range = ExponentialRange(0, 7, 1/4)
    words_a = random_words(exp_range.max)
    words_b = random_words(exp_range.max)

    with timed_report():
        for i in exp_range.iterator(4):
            very_slow_match_within(words_a[:i], words_b[:i])

        for i in exp_range.iterator(4):
            slow_match_within(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            fast_match_within(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            fast_intersection(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            pd_naive_index_match(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            pd_unique_index_match(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            pd_native_index_match(words_a[:i], words_b[:i])


    print('words_a', len(words_a), len(set(words_a)))
    print('words_a', len(words_b), len(set(words_b)))

    exp_range = ExponentialRange(0, 8, 1/4)
    words_a = random_characters(exp_range.max)
    words_b = random_characters(exp_range.max)

    with timed_report():
        for i in exp_range.iterator(5):
            very_slow_match_within(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            slow_match_within(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            fast_match_within(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            fast_intersection(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            pd_naive_index_match(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            pd_unique_index_match(words_a[:i], words_b[:i])

        for i in exp_range.iterator():
            pd_native_index_match(words_a[:i], words_b[:i])


    print('words_a', len(words_a), len(set(words_a)))
    print('words_a', len(words_b), len(set(words_b)))

