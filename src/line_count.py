"""
Given a file full of random numbers and random columns, 
count the lines in the file
"""

import os
import re

import pandas as pd
import numpy as np
from numba import jit
import csv
import mmap
from typing import List

from utils.profiler import time_this, timed_report
from utils.profiler import ExponentialRange


src_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(
    src_dir, 
    '..', 
    'data',
    'big_numeric_csv_files',
)

lc_reg = re.compile(r'file_[A-Z]{1,2}_rows_([0-9]+)\.csv')

def get_data_files() -> List[str]:
    files = os.listdir(data_dir)
    files.sort()
    return [os.path.join(data_dir, f) for f in files]

def get_line_count_from_filepath(filepath):
    filename = os.path.basename(filepath)
    match = re.match(lc_reg, filename)
    if match:
        return int(match.group(1))
    raise ValueError('File name did not match pattern.')

_get_lc = get_line_count_from_filepath


@time_this(lambda *args, **kwargs: _get_lc(args[0]))
def slow_count_lines(filepath):
    """
    Counts lines by reading entire file into memory as a 
    list of lines represented by strings
    """
    with open(filepath, 'r') as file_ptr:
        lines: List[str] = file_ptr.readlines()
        line_count = len(lines)
    return line_count



@time_this(lambda *args, **kwargs: _get_lc(args[0]))
def csv_slow_count_lines(filepath):
    """
    Counts lines by parsing the csv file line-by-line
    """
    with open(filepath, 'r') as file_ptr:
        csv_reader = csv.reader(file_ptr, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
    return line_count    

@time_this(lambda *args, **kwargs: _get_lc(args[0]))
def medium_count_lines(filepath):
    """
    Counts lines by reading entire file into memory as a 
    string then counting line breaks
    """
    with open(filepath, 'r') as file_ptr:
        file_str: List[str] = file_ptr.read()
        line_count = file_str.count('\n')
    return line_count


@time_this(lambda *args, **kwargs: _get_lc(args[0]))
def fast_count_lines(filepath):
    """
    Counts lines by iterating through the file directly from
    the disk, reading each line in one at a time
    """
    with open(filepath, 'r') as file_ptr:
        line_count = 0
        for line in file_ptr:
            line_count += 1

    return line_count


@time_this(lambda *args, **kwargs: _get_lc(args[0]))
def fast_mem_map_count(filename):
    """
    Create a memory-mapping in order to count the lines
    """
    with open(filename, 'r+') as file_ptr:
        memory_map = mmap.mmap(file_ptr.fileno(), 0)
        line_count = 0
        while memory_map.readline():
            line_count += 1
    return line_count


@time_this(lambda *args, **kwargs: _get_lc(args[0]))
def np_naive_count_lines(filepath):
    """
    Counts lines by parsing file into a numpy array
    """
    data = np.genfromtxt(
        filepath, 
        delimiter=',', 
        skip_header=True
    )
    return data.shape[0]


@time_this(lambda *args, **kwargs: _get_lc(args[0]))
def pd_naive_count_lines(filepath):
    """
    Counts lines by parsing file into a pd.DataFrame
    """
    df = pd.read_csv(filepath)
    return df.shape[0]


# Document this somehwere
def wccount(filename):
    out = subprocess.Popen(['wc', '-l', filename],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT
                         ).communicate()[0]
    return int(out.partition(b' ')[0])

if __name__ == '__main__':

    # filepaths = get_data_files()[:10]
    # for filepath in filepaths:
    #     print(get_line_count_from_filepath(filepath))
    #     print(slow_count_lines(filepath))
    #     print(csv_slow_count_lines(filepath))
    #     print(medium_count_lines(filepath))
    #     print(fast_count_lines(filepath))
    #     print(np_naive_count_lines(filepath))
    #     print(pd_naive_count_lines(filepath))
    #     print(fast_mem_map_count(filepath))

    filepaths = get_data_files()

    with timed_report():
        for filepath in filepaths:
            slow_count_lines(filepath)

        for filepath in filepaths:
            csv_slow_count_lines(filepath)

        for filepath in filepaths:
            medium_count_lines(filepath)

        for filepath in filepaths:
            fast_count_lines(filepath)

        for filepath in filepaths:
            fast_mem_map_count(filepath)

        for filepath in filepaths[:-4]:
            np_naive_count_lines(filepath)

        for filepath in filepaths[:-4]:
            pd_naive_count_lines(filepath)


