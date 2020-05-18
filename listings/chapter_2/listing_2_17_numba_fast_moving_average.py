@jit(nopython=True)
def _numba_fast_moving_avg(values: np.ndarray, 
    m: int=20) -> np.ndarray:
    """
    This is O(n) time and just-in-time compiled with numba
    """

    # Initialize arrays to store data
    moving_avg = np.empty(values.shape)
    moving_avg[:m-1] = np.nan

    # Exit early if m greater than length of values
    if m > values.shape[0]:
        return moving_avg

    # Compute the initial values
    accumulator = np.sum(values[:m])
    moving_avg[m-1] = accumulator / m

    # Loop through the remainder of the data
    for i in range(m, values.shape[0]):

        # Subtract the out-of-window value
        accumulator -= values[i-m]

        # Add the new in-window value
        accumulator += values[i]

        # Store the average
        moving_avg[i] = accumulator / m

    return moving_avg

# Get numba to run the jit optimization
_numba_fast_moving_avg(np.random.random(100000))

def numba_fast_moving_avg(values: np.ndarray, 
    m: int=20) -> np.ndarray:
    return _numba_fast_moving_avg(values, m=m)