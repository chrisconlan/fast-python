def bisect_search_in(values: List[float], 
    target: float) -> bool:
    """
    Given a list of floats that are assumed to be sorted, 
    determine if an element is in the list using Python's 
    bisect library. This is O(log(n))
    """

    # Find the insertion point of target within values to 
    # maintain search order using binary search
    i = bisect.bisect_left(values, target)

    # If in bounds, make comparison
    if 0 <= i < len(values):
        return values[i] == target

    # Otherwise it is definitely not a match
    return False