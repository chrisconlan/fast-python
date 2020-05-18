def _binary_search_in(values: np.ndarray, 
    target: float) -> bool:
    """
    Recursive part of binary_search_in
    """

    # Split list in half
    n = len(values)
    i = n // 2
        
    if n > 1: 
        # Search the upper or lower part of the list
        if target >= values[i]:
            return _binary_search_in(values[i:], target)
        else:
            return _binary_search_in(values[:i], target)
    else:
        # Else, test for equality
        return values[i] == target

def binary_search_in(values: np.ndarray, 
    target: float) -> bool:
    """
    Given a numpy array of floats that are assumed to be 
    sorted, determine if an element is in it. We use numpy 
    arrays here because it is important that array slices 
    are passed by reference, rather than copied.
    This is O(log(n))
    """
    return _binary_search_in(values, target)