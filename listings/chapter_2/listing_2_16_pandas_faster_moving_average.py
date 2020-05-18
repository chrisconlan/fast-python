def pd_faster_moving_avg(values: pd.Series,
    m: int=20) -> pd.Series:
    """
    This is O(n) time an outperforms the .rolling variant
    """
    cumsum = values.cumsum()
    return (cumsum - cumsum.shift(m)) / m