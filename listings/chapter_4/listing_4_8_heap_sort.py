def heap_sort(values: List[float]) -> List[float]:
    """
    Heap sort converts values to a list-based heap, then 
    extracts the root iteratively until it has achieved a 
    sorted list.

    O(n*log(n)) complexity
    """
    n = len(values)

    values = build_max_heap(values)

    # Successively move the root node to the top
    for i in range(n-1, 0, -1):

        # Store the current root node as i
        values[i], values[0] = values[0], values[i]

        # Heapify the remaining values
        _heapify(values, i, 0)

    return values