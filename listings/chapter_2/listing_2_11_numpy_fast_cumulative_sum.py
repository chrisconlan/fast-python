def np_fast_cusum(values: np.ndarray) -> np.ndarray:
    """
    This is O(n) and optimized with C code
    """
    return values.cumsum()