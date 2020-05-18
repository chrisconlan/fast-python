"""
Generate sample CSV files for file-reading tests
"""
import numpy as np
import pandas as pd
import os
import string
import itertools

from utils.profiler import ExponentialRange

src_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(src_dir, '..', 'data')
target_dir = os.path.join(data_dir, 'big_numeric_csv_files')

# Max size in rows as a power of ten
exp_range = ExponentialRange(0, 7, 1/4)
num_cols = 10
col_names = list(string.ascii_uppercase[:num_cols])

_data = np.random.random((exp_range.max, num_cols))
data = pd.DataFrame(_data, columns=col_names)

_letters = string.ascii_uppercase
_file_codes = itertools.product(_letters, repeat=2)
_file_codes = list(_file_codes)[:exp_range.max]
file_codes = [''.join(code) for code in _file_codes]

for j, i in enumerate(exp_range.iterator()):
    code = file_codes[j]
    filename = f'file_{code}_rows_{i}.csv'
    filepath = os.path.join(target_dir, filename)
    data.iloc[:i].to_csv(filepath, index=False)



