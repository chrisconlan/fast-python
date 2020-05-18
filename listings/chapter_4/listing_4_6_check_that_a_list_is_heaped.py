def assert_is_heaped(values: List[float]):
    """
    Checks that the values of a list satisfy the max-heap 
    conditions where the children of element i are located 
    at 2*i+1 and 2*i+2. 
    """
    n = len(values)
    msg = 'Did not satisfy heap condition.'
    for i in range(n):
        l = 2 * i + 1
        r = 2 * i + 2   

        if l < n:
            assert values[i] >= values[l], msg

        if r < n:
            assert values[i] >= values[r], msg