def python_fast_cusum(values: List[float]) -> List[float]:
    """
    This is O(n) time, because it does n additions for n 
    values
    """
    cusum = []
    accumulator = 0

    for value in values:
        accumulator += value
        cusum.append(accumulator)

    return cusum