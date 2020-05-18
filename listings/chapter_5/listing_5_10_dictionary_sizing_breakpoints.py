import sys

from utils.profiler import ExponentialRange
exp_range = ExponentialRange(0, 7, 1/8)

for i in exp_range.iterator():
    _dict = {j: j**2 for j in range(i)}
    _dict_size = sys.getsizeof(_dict)
    print(f'{len(_dict):<8} keys {_dict_size:>12} bytes')

# Returns ...
# 1        keys          248 bytes
# 2        keys          248 bytes
# 3        keys          248 bytes
# 4        keys          248 bytes
# 5        keys          248 bytes
# 7        keys          376 bytes
# 10       keys          376 bytes
# 13       keys          656 bytes
# 17       keys          656 bytes
# 23       keys         1192 bytes
# 31       keys         1192 bytes
# 42       keys         1192 bytes
# 56       keys         2288 bytes
# 74       keys         2288 bytes
# 100      keys         4712 bytes
# ...