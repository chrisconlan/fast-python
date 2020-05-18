def _partition(values: List[float], l: int, r: int):
    """
    Move l and r inward, swapping where appropriate. Return 
    the crossover index as a partition value for future 
    recursions of the function
    """

    # Grab some middle value as the pivot
    # Index can be a random integer in (l,r) or a midpoint
    pivot = values[(l + r) // 2]

    # Make appropriate swaps until l and r cross over
    while l <= r:

        # Find an element on the left that should be on the
        # right
        while values[l] < pivot:
            l += 1

        # Find an element on the right that should be on 
        # the left
        while values[r] > pivot:
            r -= 1

        # If l and r did not cross over, make a swap
        if l <= r:
            values[l], values[r] = values[r], values[l]
            l += 1
            r -= 1

    return l
    
def _quick_sort(values: List[float], l: int, r: int):
    """
    Sorts values in-place by recursively swapping values 
    around a pivot point

    l is a 'lefthand' index and r is a 'righthand' per the 
    algorithm
    """
    i = _partition(values, l, r)
    if l < i - 1:
        _quick_sort(values, l, i-1)
    if i < r:
        _quick_sort(values, i, r)
        
def quick_sort(values: List[float]):
    """
    Wrapper around the main quick_sort logic
    """
    n = len(values)
    _quick_sort(values, 0, n-1)