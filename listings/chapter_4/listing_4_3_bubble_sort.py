def bubble_sort(values: List[float]) -> List[float]:
    """
    Bubble sorting is O(n^2) complexity and modifies the 
    list in-place
    """
    n = len(values)

    # Set to true so that loop happens at least once
    swap_occurred = True
    while swap_occurred:

        # Consider finished if no swaps happen
        swap_occurred = False
        for i in range(n-1):

            # If something is out of order ...
            if values[i] > values[i+1]:

                # Swap the values
                values[i], values[i+1] = \
                    values[i+1], values[i]

                # Mark that we are unfinished because 
                # we swapped something
                swap_occurred = True

    # Return a reference to the list
    return values