def slow_cusum_expanded(values: List[float]) -> List[float]:
    """
    Same as the above, O(n^2), but exposes the hidden 
    complexity of sum()
    """
    cusum = []

    for i in range(len(values)):

        accumulator = 0
        for j in range(i+1):
            accumulator += values[j]

        cusum.append(accumulator)

    return cusum