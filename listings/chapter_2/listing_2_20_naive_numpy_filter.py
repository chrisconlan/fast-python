def numpy_naive_filter(values: np.ndarray, 
    weights: np.ndarray, a: int) -> np.ndarray:
    """
    This is O(nm) for a list of length n and weights of 
    length m because it makes no assumptions about the 
    shape of the weighting vector
    """

    n, m = values.shape[0], weights.shape[0]
    b = a + m - 1

    # Exit early if m greater than length of values
    if m > n or -a > n or b > n:
        return np.array([np.nan]*n)

    # Front and back padding of series
    front_pad = max(-a, 0)
    back_pad = max(b, 0)

    # Initialize the output array
    y = np.empty((n,))

    # Pad with na values
    y[:front_pad] = np.nan
    y[-back_pad:] = np.nan

    # Compute the filter
    for i in range(front_pad, n - back_pad):
        y[i] = weights.dot(values[(i+a):(i+a+m)])

    return y