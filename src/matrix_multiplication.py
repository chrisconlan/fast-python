

"""
Given a list of numbers, compute their cumulative sum
Output the cumulative sum to a new sequence
"""
import pandas as pd
from numba import jit
import numpy as np

from typing import List, Tuple, NewType

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

ListMatrix = NewType('ListMatrix', List[List[float]])

def random_numeric_list(n: int) -> List[float]:
    return list(np.random.random(n))


def random_matrices(
    n: int) -> Tuple[np.ndarray, np.ndarray]:

    a = np.random.random((n,n))
    b = np.random.random((n,n))

    return a, b


def matrix_to_nested_list(a: np.ndarray) -> ListMatrix:
    return [[v for v in row] for row in a]


@time_this(lambda *args, **kwargs: len(args[0]))
def list_multiply(a: ListMatrix, 
    b: ListMatrix) -> ListMatrix:
    """
    Multiply matrices a x b. This is O(n^3).
    """

    # Assume all inner lists are same length
    n, m, p = len(a), len(a[0]), len(b[0])
    assert m == len(b), 'Inner dimensions do not match.'

    # Create a nested list with n rows and p columns
    result = [[0]*p for _ in range(n)]

    # Add it all up
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += a[i][k] * b[k][j]

    return result


@time_this(lambda *args, **kwargs: len(args[0]))
def matrix_multiply(a: np.ndarray, 
    b: np.ndarray) ->  np.ndarray:
    """
    Multiply matrices a x b. This is O(n^3).
    """
    return a.dot(b)

    


if __name__ == '__main__':

    # a, b = random_matrices(10)
    # a_list = matrix_to_nested_list(a)
    # b_list = matrix_to_nested_list(b)

    # print(list_multiply(a_list, b_list))
    # print(matrix_to_nested_list(a.dot(b)))

    exp_range = ExponentialRange(0, 4, 1/4)
    a, b = random_matrices(exp_range.max)

    with timed_report():
        for i in exp_range.iterator(2):
            a_list = matrix_to_nested_list(a[:i, :i])
            b_list = matrix_to_nested_list(b[:i, :i])
            list_multiply(a_list[:i], b_list[:i])

        for i in exp_range.iterator():
            matrix_multiply(a[:i, :i], b[:i, :i])

