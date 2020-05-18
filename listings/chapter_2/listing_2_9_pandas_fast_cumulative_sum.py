def pandas_fast_cusum(values: pd.Series) -> pd.Series:
    """
    This is O(n) and optimized with C code
    """
    return values.cumsum()
