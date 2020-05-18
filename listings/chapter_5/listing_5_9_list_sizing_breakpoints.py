import sys

for i in range(100):
    _list = [(j+0.1)**2 for j in range(i)]
    _list_size = sys.getsizeof(_list)
    print(f'{len(_list):<8} values {_list_size:>12} bytes')

# Returns ...
# 0        values           72 bytes
# 1        values          104 bytes
# 2        values          104 bytes
# 3        values          104 bytes
# 4        values          104 bytes
# 5        values          136 bytes
# 6        values          136 bytes
# 7        values          136 bytes
# 8        values          136 bytes
# 9        values          200 bytes
# 10       values          200 bytes
# 11       values          200 bytes
# 12       values          200 bytes
# 13       values          200 bytes
# ...

from utils.profiler import ExponentialRange
exp_range = ExponentialRange(0, 7, 1/4)

for i in exp_range.iterator():
    _list = [(j+0.1)**2 for j in range(i)]
    _list_size = sys.getsizeof(_list)
    print(f'{len(_list):<8} values {_list_size:>12} bytes')

# Returns ...
# 1        values          104 bytes
# 3        values          104 bytes
# 5        values          136 bytes
# 10       values          200 bytes
# 17       values          272 bytes
# 31       values          352 bytes
# 56       values          536 bytes
# 100      values          920 bytes
# 177      values         1680 bytes
# 316      values         2904 bytes
# 562      values         4856 bytes
# 1000     values         9032 bytes
# ...