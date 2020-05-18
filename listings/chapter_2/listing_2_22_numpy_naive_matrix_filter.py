def numpy_naive_matrix_filter(values: np.ndarray, 
    weights: np.ndarray, a: int) -> np.ndarray:
    """
    This is O(nm) for a list of length n and weights of 
    length m. Takes advantage of duplicate weights to save 
    calculations.
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
    y = np.zeros((n,))

    # Pad with na values
    y[:front_pad] = np.nan
    y[-back_pad:] = np.nan

    # Build a matrix to multiply with weight vector
    q = np.empty((n - front_pad - back_pad, m))
    for j in range(m):
        q[:,j] = values[j:(j+n-m+1)]

    y[front_pad:-back_pad] = q.dot(weights)

    return y