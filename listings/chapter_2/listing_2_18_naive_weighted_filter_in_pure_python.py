def naive_filter(values: List[float], weights: List[float], 
    a: int) -> List[float]:
    """
    This is O(nm) for a list of length n and weights of 
    length m because it makes no assumptions about the 
    shape of the weighting vector
    """

    n, m = len(values), len(weights)
    b = a + m - 1

    # Exit early if m greater than length of values
    if m > n or -a > n or b > n:
        return [None] * len(values)

    # Front and back padding of series
    front_pad = max(-a, 0)
    back_pad = max(b, 0)

    # Apply front pad
    y = [None] * front_pad

    # Compute the filter
    for i in range(front_pad, n - back_pad):
        accumulator = 0
        for j in range(m):
            accumulator += weights[j] * values[i+j+a]
        y.append(accumulator)

    # Apply back pad
    y.extend([None] * back_pad)

    return y