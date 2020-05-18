def pd_fast_moving_avg(values: pd.Series,
    m: int=20) -> pd.Series:
    """
    This is O(n) time and utilizes pandas .rolling interface
    """
    return values.rolling(m).mean()