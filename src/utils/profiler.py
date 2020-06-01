from timeit import default_timer
import pandas as pd
from contextlib import contextmanager
from typing import List, Dict, Any, Callable
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import os
import re
import numpy as np

mpl.rcParams['grid.color'] = 'k'
mpl.rcParams['grid.linestyle'] = ':'
mpl.rcParams['grid.linewidth'] = 0.5

# To help printing results
pd.set_option('display.max_rows', None)

# Flip this to false to skip chart rendering. Mostly for bulk testing.
SHOW = True

__all__ = ["time_this", "report_results", "timed_report", "ExponentialRange"]
# A module-level store of all the evaluation times of things you ran with the 
# @time_this decorator
runtime_table: List[Dict[str, Any]] = list()

def clear_runtime_table():
    """
    Empty out the runtime table in-between reports
    """
    del runtime_table[:]

def time_this(length_method: Callable[[Any], int]):
    """
    A decorator that stores the evaluation time against a user-defined length 
    and plots it.

    Usage: 
        @time_this(lambda x: len(x))
        def some_function(x, y, z):
            # do something ...

        # or ...
        @time_this(lambda *args, **kwargs: len(args[0]))
        def some_function(x, y, z):
            # do something ...
    """
    def _time_this(method):

        def timed_function(*args, **kwargs):
            ts = default_timer()
            result = method(*args, **kwargs)
            te = default_timer()
            print(f'{method.__name__}')

            n = length_method(*args, **kwargs)
            t = (te - ts) * 1000
            n_over_t = round(n / t, 4)
            print(f'    n   = {n} values')
            print(f'    t   = {round(t, 3)} ms')
            print(f'    n/t = {n_over_t} values per ms')
            print()
            runtime_table.append({
                'function': method.__name__,
                'n_values': n,
                't_milliseconds': round(t, 3),
                'values_per_ms': n_over_t,
            })
            return result

        return timed_function

    return _time_this



def report_results():
    """
    Plot and print some information about the efficiency of the algorithms you
    just ran
    """

    # Print the run-time table
    df = pd.DataFrame(runtime_table)
    print(df)

    # Build and plot the runtime chart
    pivot_table = df.pivot(
        index='n_values',
        columns='function',
        values='t_milliseconds',
    )
    ax = pivot_table.plot(
        logx=True,
        logy=True,
        title='Milliseconds to complete',
    )
    ax.set_ylabel('milliseconds')
    ax.set_xlabel('input length')
    plt.grid()

    # Build and plot the efficiency chart
    pivot_table = df.pivot(
        index='n_values',
        columns='function',
        values='values_per_ms',
    )
    ax = pivot_table.plot(
        logx=True,
        logy=True,
        title='Values processed per millisecond',
    )
    ax.set_ylabel('values per millisecond')
    ax.set_xlabel('input length')
    plt.grid()

    if SHOW:
        plt.show()


@contextmanager
def timed_report():
    """
    e a s e   o f   u s e
    """
    yield
    report_results()
    clear_runtime_table()


ONE_FOURTH = 1/4

class ExponentialRange(object):
    """
    A range that operates on exponents of 10, inclusive
    """

    def __init__(self, start_exponent: int, end_exponent: int, 
        step_size: float=ONE_FOURTH, int_only: bool=True):

        self.step_size = step_size
        self.start = self.exp_to_int(start_exponent)
        self.end = self.exp_to_int(end_exponent)
        self.int_only = int_only

    def exp_to_int(self, end_exponent: int):
        return math.ceil(end_exponent / self.step_size)

    def get_element(self, i):
        """
        Get the i-th element of the iteration
        """
        val = 10 ** (i * self.step_size)
        if self.int_only:
            return int(val)
        return val

    def iterator(self, alt_end: int=None):
        """
        Yield unique values of get_element for i in start through end
        """
        existing_entries = set()

        start = self.start

        if alt_end:
            end = self.exp_to_int(alt_end)
        else:
            end = self.end

        for i in range(start, end + 1):
            value = self.get_element(i)
            if not value in existing_entries:
                yield value
            existing_entries.add(value)        

    def np_range(self):
        return np.array([*self.iterator()])

    @property
    def max(self):
        return self.get_element(self.end)

