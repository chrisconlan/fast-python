"""
Timing various string operations
"""

import sys
import string

for i in range(10):
    some_string = string.ascii_lowercase[:i]
    string_size = sys.getsizeof(some_string)
    print(f'{some_string:<10}{string_size:>4} bytes')

# Returns ...
#             49 bytes
# a           50 bytes
# ab          51 bytes
# abc         52 bytes
# abcd        53 bytes
# abcde       54 bytes
# abcdef      55 bytes
# abcdefg     56 bytes
# abcdefgh    57 bytes
# abcdefghi   58 bytes
