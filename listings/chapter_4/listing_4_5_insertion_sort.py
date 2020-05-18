def insertion_sort(values: List[float]) -> List[float]:
    """
    Insertion sort is O(n^2) complexity and modifies the 
    list in-place
    """
    n = len(values)

    # Prepare to insert the i-th element in the appropriate
    # place, over and over
    for i in range(1, n):

        # Keep track of initial i-th value because it might
        # get overwritten
        value_to_insert = values[i]

        # Descend j-1 to 0 looking for a home for i
        j = i-1
        while j >= 0 and values[j] > value_to_insert:

            # Shift the larger values up along the way
            values[j+1] = values[j]

            # Descend further
            j -= 1

        # Insert the i-th value in the right place
        if i != j+1:
            values[j+1] = value_to_insert

    # Return a reference to the list
    return values