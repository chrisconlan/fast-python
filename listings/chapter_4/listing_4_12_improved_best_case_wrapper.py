def improved_best_case_wrapper(values: List[float], 
    sorting_algo: Callable[[List], List]) -> List[float]:
    """
    Wrap any sorting algorithm with this in order to convert
    its best-case complexity to O(n)
    """
    n = len(values)
    
    # Check if it is sorted
    is_sorted = all(
        values[i] <= values[i+1] for i in range(n-1)
    )
    
    # Just return if sorted
    if is_sorted:
        return values
        
    # Fall back on the real sorting algo
    return sorting_algo(values)
    
values = improved_best_case_wrapper(values, insertion_sort)