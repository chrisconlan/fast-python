import random
import string
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


@time_this(lambda *args, **kwargs: len(args[1]))
def naive_in_operator(value: str, 
    sequence: List[str]) -> bool:
    """
    Check if a value is in the sequence, naively

    This is O(n) for sequence of length n
    """
    is_in = False
    for other_value in sequence:
        if value == other_value:
            is_in = True
    return is_in


@time_this(lambda *args, **kwargs: len(args[1]))
def early_stopping_in_operator(value: str, 
    sequence: List[str]) -> bool:
    """
    Check if a value is in the sequence with early stopping

    This is O(n) for sequence of length n
    """
    for other_value in sequence:
        if value == other_value:
            return True
    return False


@time_this(lambda *args, **kwargs: len(args[1]))
def native_in_operator(value: str,
    sequence: List[str]) -> bool:
    """
    Use Python's native in operator to check if a value is 
    in a sequence

    This is O(n) for sequence of length n
    """
    return value in sequence


if __name__ == '__main__':

    # print(naive_in_operator('A', ['A', 'B', 'C']))
    # print(early_stopping_in_operator('A', ['A', 'B', 'C']))
    # print(native_in_operator('A', ['A', 'B', 'C']))

    exp_range = ExponentialRange(0, 7, 1/4)
    words = random_words(exp_range.max)
    value = words[10000]

    with timed_report():
        for i in exp_range.iterator():
            naive_in_operator(value, words[:i])

        for i in exp_range.iterator():
            early_stopping_in_operator(value, words[:i])

        for i in exp_range.iterator():
            native_in_operator(value, words[:i])
