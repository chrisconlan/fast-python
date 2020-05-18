def np_fast_moving_avg(values: List[float], 
    m: int=20) -> List[float]:
    """
    Calculate the moving average in numpy in O(n) time. 
    Calculate v_i in advance using lagged difference of the 
    cumsum.
    """

    # Calculate the cumulative sum to derive v_i from
    cumsum = np.cumsum(values)

    # Initialize empty array
    moving_avg = np.empty((len(values),))

    # Fill it with results
    moving_avg[:m-1] = np.nan

    if m <= values.shape[0]:
        moving_avg[m-1] = cumsum[m-1] / m

    if m < values.shape[0]:
        moving_avg[m:] = (cumsum[m:] - cumsum[:-m]) / m

    return moving_avg