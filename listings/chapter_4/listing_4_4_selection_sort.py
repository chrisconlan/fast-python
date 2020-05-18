def selection_sort(values: List[float]) -> List[float]:
    """
    Selection sort is O(n^2) complexity and modifies the 
    list in-place
    """
    n = len(values)

    # Prepare to swap i with the lowest value above it
    for i in range(n):

        # Set i as the defeault value of the swap target
        min_idx = i

        # Loop through elements above i
        for j in range(i+1, n):

            # If anything is less than j, prepare to put 
            # it in the i-th position
            if values[j] < values[min_idx]:
                min_idx = j

        # Make the swap
        values[i], values[min_idx] = \
            values[min_idx], values[i]

    # Return a reference to the list
    return values
