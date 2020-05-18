def fast_moving_avg(values: List[float], 
    m: int=20) -> List[float]:
    """
    This is O(n) for a list of length n because it 
    uses the differential of the accumulator at each step
    """

    # Exit early if m greater than length of values
    if m > len(values):
        return [None] * len(values)

    # Pad initial m-1 values with Nones
    moving_avg = [None] * (m-1)

    # Compute the initial values
    accumulator = sum(values[:m])
    moving_avg.append(accumulator / m)

    # Loop through the remainder of the data
    for i in range(m, len(values)):

        # Subtract the out-of-window value
        accumulator -= values[i-m]

        # Add the new in-window value
        accumulator += values[i]

        # Store the average
        moving_avg.append(accumulator / m)

    return moving_avg