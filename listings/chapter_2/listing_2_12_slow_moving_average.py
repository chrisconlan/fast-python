def slow_moving_avg(values: List[float], 
    m: int=20) -> List[float]:
    """
    This is O(nm) for a list of length n because it 
    re-computes the average at each step
    """

    # Exit early if m greater than length of values
    if m > len(values):
        return [None] * len(values)

    # Pad initial m-1 values with Nones
    moving_avg = [None] * (m-1)

    # Compute the moving average
    for i in range(m-1, len(values)):
        the_avg = sum(values[(i-m+1):(i+1)]) / m
        moving_avg.append(the_avg)

    return moving_avg