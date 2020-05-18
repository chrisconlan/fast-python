def naive_in_operator(values: List[float], 
    target: float) -> bool:
    """
    Given a list of floats that are assumed to be sorted, 
    determine if an element is in the list with early 
    stopping. This is O(n)
    """
    for value in values:
        if target == value:
            return True