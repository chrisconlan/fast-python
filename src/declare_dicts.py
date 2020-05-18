"""
Sizing information for dictionaries
"""
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
# 133      keys         4712 bytes
# 177      keys         9328 bytes
# 237      keys         9328 bytes
# 316      keys         9328 bytes
# 421      keys        18536 bytes
# 562      keys        18536 bytes
# 749      keys        36976 bytes
# 1000     keys        36976 bytes
# 1333     keys        36976 bytes
# 1778     keys        73832 bytes
# 2371     keys        73832 bytes
# 3162     keys       147568 bytes
# 4216     keys       147568 bytes
# 5623     keys       295016 bytes
# 7498     keys       295016 bytes
# 10000    keys       295016 bytes
# 13335    keys       589936 bytes
# 17782    keys       589936 bytes
# 23713    keys      1310824 bytes
# 31622    keys      1310824 bytes
# 42169    keys      1310824 bytes
# 56234    keys      2621552 bytes
# 74989    keys      2621552 bytes
# 100000   keys      5242984 bytes
# 133352   keys      5242984 bytes
# 177827   keys     10485872 bytes
# 237137   keys     10485872 bytes
# 316227   keys     10485872 bytes
# 421696   keys     20971624 bytes
# 562341   keys     20971624 bytes
# 749894   keys     41943152 bytes
# 1000000  keys     41943152 bytes
# 1333521  keys     41943152 bytes
# 1778279  keys     83886184 bytes
# 2371373  keys     83886184 bytes
# 3162277  keys    167772272 bytes
# 4216965  keys    167772272 bytes
# 5623413  keys    335544424 bytes
# 7498942  keys    335544424 bytes
# 10000000 keys    335544424 bytes




