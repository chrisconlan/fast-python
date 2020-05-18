def smart_filter(values: List[float], weights: List[float], 
    a: int) -> List[float]:
    """
    This is O(nm) for a list of length n and weights of 
    length m. Takes advantage of duplicate weights to save 
    calculations.
    """

    n, m = len(values), len(weights)
    b = a + m - 1

    # Exit early if m greater than length of values
    if m > n or -a > n or b > n:
        return [None] * len(values)

    # Front and back padding of series
    front_pad = max(-a, 0)
    back_pad = max(b, 0)

    # Pre-compute scaled values for each unique weight
    unique_weights: Set[float] = set(weights)
    scaled_vectors: Dict[float, List[float]] = dict()
    for w in unique_weights:
        scaled_vectors[w] = [w * v for v in values]

    # Apply front pad
    y = [None] * front_pad

    # Compute the moving average
    for i in range(front_pad, n - back_pad):
        accumulator = 0
        for j, w in enumerate(weights):
            accumulator += scaled_vectors[w][i+j+a]
        y.append(accumulator)

    # Apply back pad
    y.extend([None] * back_pad)

    return y