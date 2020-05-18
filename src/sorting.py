"""
Given a list of numbers, sort it.
"""
import random
import string
import numpy as np
import pandas as pd
from typing import List, Tuple, Set, Dict

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange

def random_numeric_list(n: int) -> List[float]:
    return list(np.random.random(n))


@time_this(lambda *args, **kwargs: len(args[0]))
def bubble_sort(values: List[float]) -> List[float]:
    """
    Bubble sorting is O(n^2) complexity and modifies the 
    list in-place
    """
    n = len(values)

    # Set to true so that loop happens at least once
    swap_occurred = True
    while swap_occurred:

        # Consider finished if no swaps happen
        swap_occurred = False
        for i in range(n-1):

            # If something is out of order ...
            if values[i] > values[i+1]:

                # Swap the values
                values[i], values[i+1] = \
                    values[i+1], values[i]

                # Mark that we are unfinished because 
                # we swapped something
                swap_occurred = True

    # Return a reference to the list
    return values

@time_this(lambda *args, **kwargs: len(args[0]))
def selection_sort(values: List[float]) -> List[float]:
    """
    Selection sort is O(n^2) complexity and modifies the 
    list in-place
    """
    n = len(values)

    # Prepare to swap i with the lowest value above it
    for i in range(n):

        # Set i as the defeault value of the swap target
        min_idx = i

        # Loop through elements above i in position
        for j in range(i+1, n):

            # If anything is less than j, prepare to put 
            # it in the i-th position
            if values[j] < values[min_idx]:
                min_idx = j

        # Make the swap
        values[i], values[min_idx] = \
            values[min_idx], values[i]

    # Return a reference to the list
    return values

@time_this(lambda *args, **kwargs: len(args[0]))
def insertion_sort(values: List[float]) -> List[float]:
    """
    Insertion sort is O(n^2) complexity and modifies the 
    list in-place
    """
    n = len(values)

    # Prepare to insert the i-th element in the appropriate
    # place, over and over
    for i in range(1, n):

        # Keep track of initial i-th value because it might
        # get overwritten
        value_to_insert = values[i]

        # Descend j-1 to 0 looking for a home for i
        j = i-1
        while j >= 0 and values[j] > value_to_insert:

            # Shift the larger values up along the way
            values[j+1] = values[j]

            # Descend further
            j -= 1

        # Insert the i-th value in the right place if
        # if j changed
        if i != j+1:
            values[j+1] = value_to_insert

    # Return a reference to the list
    return values

def assert_is_heaped(values: List[float]):
    """
    Checks that the values of a list satisfy the max-heap 
    conditions where the children of element i are located 
    at 2*i+1 and 2*i+2. 
    """
    n = len(values)
    msg = 'Did not satisfy heap condition.'
    for i in range(n):
        l = 2 * i + 1
        r = 2 * i + 2   

        if l < n:
            assert values[i] >= values[l], msg

        if r < n:
            assert values[i] >= values[r], msg


def _heapify(values: List[float], heap_size: int, 
    root_node: int):
    """
    The ubiquitous heapify function that handles both heap 
    construction and root extraction on a list-based heap, 
    where the children of element i are located at 
    2*i+1 and 2*i+2. 
    """
    n = heap_size

    # Index of the root
    i = root_node

    # Default index of the largest value
    j = root_node

    # Probe these elements as potential roots
    l = 2 * i + 1 # Index of left child node
    r = 2 * i + 2 # Index of right child node

    # Set j to the largest value of a child
    if l < n and values[l] > values[i]:
        j = l

    if r < n and values[r] > values[j]:
        j = r

    # If the root is not the max, set a new root and send 
    # it back through
    if j != i:
        # Swap max and root elements
        values[i], values[j] = values[j], values[i]

        # Recurse
        _heapify(values, n, j)

# @time_this(lambda *args, **kwargs: len(args[0]))
def build_max_heap(values: List[float]) -> List[float]:
    """
    Converts values into a max heap.
    """
    n = len(values)

    # Create a max-heap from values
    for i in range(n, -1, -1):
        _heapify(values, n, i)

    # Return a reference to values
    return values

@time_this(lambda *args, **kwargs: len(args[0]))
def heap_sort(values: List[float]) -> List[float]:
    """
    Heap sort converts values to a list-based heap, then 
    extracts the root iteratively until it has achieved a 
    sorted list.

    O(n*log(n)) complexity
    """
    n = len(values)

    values = build_max_heap(values)

    # Successively move the root node to the top
    for i in range(n-1, 0, -1):

        # Store the current root node as i
        values[i], values[0] = values[0], values[i]

        # Heapify the remaining values
        _heapify(values, i, 0)

    return values


def _merge(left: List[float], 
    right: List[float]) -> List[float]:
    """
    Merging part of the merge_sort algorithm. 
    """
    # Output
    _sorted = []

    # Left and right indexes
    l = r = 0

    # Left and right lengths
    n_left, n_right = len(left), len(right)

    # We incremenet either l or r every time, so it should 
    # take this n_left + n_right total steps to reach the 
    # end of each
    for _ in range(n_left + n_right):

        # We are still working through both right and left
        if l < n_left and r < n_right:

            # Add the smallest element and increment
            if left[l] <= right[r]:
                _sorted.append(left[l])
                l += 1
            else:
                _sorted.append(right[r])
                r += 1

        # We are at the end of the left list, add rights
        elif l == n_left:
            _sorted.append(right[r])
            r += 1

        # We are at the end of the right list, add lefts
        elif r == n_right:
            _sorted.append(left[l])
            l += 1

    return _sorted


def merge_sort(values: List[float]) -> List[float]:
    """
    Sequentially split lists into ordered pairs, then merges
    the results
    """
    n = len(values)

    # Exit early on n == 1, when all possible splits have 
    # been done
    if n == 1:
        return values

    # Index of integer midpoint
    i_mid = len(values) // 2

    left: List[float] = merge_sort(values[:i_mid])
    right: List[float] = merge_sort(values[i_mid:])

    return _merge(left, right)

@time_this(lambda *args, **kwargs: len(args[0]))
def merge_sort_timeable(values: List[float]):
    """
    Need to call this from another function in order to time
    it, since the original is recursive
    """
    return merge_sort(values)



def _partition(values: List[float], l: int, r: int):
    """
    Move l and r inward, swapping where appropriate. Return 
    the crossover index as a partition value for future 
    recursions of the function
    """

    # Grab some middle value as the pivot
    # Index can be a random integer in (l,r) or a midpoint
    pivot = values[(l + r) // 2]

    # Make appropriate swaps until l and r cross over
    while l <= r:

        # Find an element on the left that should be on the
        # right
        while values[l] < pivot:
            l += 1

        # Find an element on the right that should be on 
        # the left
        while values[r] > pivot:
            r -= 1

        # If l and r did not cross over, make a swap
        if l <= r:
            values[l], values[r] = values[r], values[l]
            l += 1
            r -= 1

    return l

def _quick_sort(values: List[float], l: int, r: int):
    """
    Sorts values in-place by recursively swapping values 
    around a pivot point

    l is a 'lefthand' index and r is a 'righthand' per the 
    algorithm
    """
    i = _partition(values, l, r)
    if l < i - 1:
        _quick_sort(values, l, i-1)
    if i < r:
        _quick_sort(values, i, r)


@time_this(lambda *args, **kwargs: len(args[0]))
def quick_sort(values: List[float]):
    """
    Wrapper around the main quick_sort logic
    """
    n = len(values)
    _quick_sort(values, 0, n-1)


@time_this(lambda *args, **kwargs: len(args[0]))
def python_native_sort(values: List[float]):
    values.sort()


def improved_best_case_wrapper(values: List[float], 
    sorting_algo) -> List[float]:
    """
    Wrap any sorting algorithm with this in order to convert
    its best-case complexity to O(n)
    """
    n = len(values)

    # Check if it is sorted
    is_sorted = all(
        values[i] <= values[i+1] for i in range(n-1)
    )
    
    # Just return if sorted
    if is_sorted:
        return values
        
    # Fall back on the real sorting algo
    return sorting_algo(values)


def assert_sorted(values):
    n = len(values)
    is_sorted = all(
        values[i] <= values[i+1] for i in range(n-1)
    )
    assert is_sorted, 'values are not sorted.'

if __name__ == '__main__':


    # values = random_numeric_list(10)
    # print(bubble_sort(values))
    # assert_sorted(values)

    # values = random_numeric_list(10)
    # print(selection_sort(values))
    # assert_sorted(values)

    # values = random_numeric_list(10)
    # print(insertion_sort(values))
    # assert_sorted(values)

    # values = random_numeric_list(10)
    # print(heap_sort(values))
    # assert_sorted(values)

    # values = random_numeric_list(10)
    # values = merge_sort_timeable(values)
    # print(values)
    # assert_sorted(values)

    # values = random_numeric_list(10)
    # quick_sort(values)
    # print(values)
    # assert_sorted(values)

    # values = random_numeric_list(10)
    # python_native_sort(values)
    # print(values)
    # assert_sorted(values)

    exp_range = ExponentialRange(0, 6, 1/4)
    values = random_numeric_list(exp_range.max)

    with timed_report():
        for i in exp_range.iterator(4):
            _values = values[:i].copy()
            bubble_sort(_values)
            assert_sorted(_values)

        for i in exp_range.iterator(4):
            _values = values[:i].copy()
            selection_sort(_values)
            assert_sorted(_values)

        for i in exp_range.iterator(4):
            _values = values[:i].copy()
            insertion_sort(_values)
            assert_sorted(_values)

        # for i in exp_range.iterator(6):
        #     _values = values[:i].copy()
        #     build_max_heap(_values)

        for i in exp_range.iterator(6):
            _values = values[:i].copy()
            heap_sort(_values)
            assert_sorted(_values)

        for i in exp_range.iterator(6):
            _values = values[:i].copy()
            _values = merge_sort_timeable(_values)
            assert_sorted(_values)

        for i in exp_range.iterator(6):
            _values = values[:i].copy()
            quick_sort(_values)
            assert_sorted(_values)

        for i in exp_range.iterator(6):
            _values = values[:i].copy()
            python_native_sort(_values)
            assert_sorted(_values)

