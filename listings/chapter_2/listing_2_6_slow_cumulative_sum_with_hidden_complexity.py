def slow_cusum(values: List[float]) -> List[float]:
    """
    This is O(n^2) time, because it computes ...
    1
    1 + 2
    1 + 2 + 3
    1 + 2 + 3 + 4
    and so on ...
    Leading to n*(n-1)/2 individual additions, 
    which is O(n^2)
    """
    cusum = []

    for i in range(len(values)):
        the_sum = sum(values[:i+1])
        cusum.append(the_sum)

    return cusum