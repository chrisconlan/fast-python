from numba import jit
import numpy as np

@jit(nopython=True)
def _numba_fast_sum(values: np.ndarray) -> float:
    """
    JIT compilation occurs after one use
    """
    accum = 0
    for value in values:
        accum += value
    return accum

# Force numba to run jit compilation
_numba_fast_sum(np.random.random(100000))

def numba_fast_sum(values: np.ndarray) -> float:
    """
    Redeclare optimized wrapper
    """
    return _numba_fast_sum(values)
