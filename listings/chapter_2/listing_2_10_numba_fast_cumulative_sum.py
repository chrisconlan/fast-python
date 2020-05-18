@jit(nopython=True)
def _numba_fast_cusum(values: np.ndarray) -> np.ndarray:
    """
    This is O(n) time and just-in-time compiled with numba
    """
    cusum = np.zeros(values.shape[0])
    accumulator = 0

    for index, value in enumerate(values):
        accumulator += value
        cusum[index] = accumulator

    return cusum

# Get numba to run the jit optimization
_numba_fast_cusum(np.random.random(100000))

def numba_fast_cusum(values: np.ndarray) -> np.ndarray:
    return _numba_fast_cusum(values)