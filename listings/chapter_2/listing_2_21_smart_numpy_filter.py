def numpy_smart_filter(values: np.ndarray, 
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

    unique_weights: Set[float] = set(weights)
    scaled_vectors: Dict[float, np.ndarray] = dict()
    for w in unique_weights:
        scaled_vectors[w] = w * values

    r1, r2 = front_pad, n-back_pad
    for j, w in enumerate(weights):
        v = scaled_vectors[w]
        y[r1:r2] += v[(r1+j+a):(r2+a+j)]

    return y