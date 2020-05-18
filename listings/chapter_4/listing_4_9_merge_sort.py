def _merge(left: List[float], 
    right: List[float]) -> List[float]:
    """
    Merging part of the merge_sort algorithm. 
    """
    # Output
    _sorted = []

    # Left and right indexes
    l = r = 0

    # Left and right lengths
    n_left, n_right = len(left), len(right)

    # We incremenet either l or r every time, so it should 
    # take this n_left + n_right total steps to reach the 
    # end of each
    for _ in range(n_left + n_right):

        # We are still working through both right and left
        if l < n_left and r < n_right:

            # Add the smallest element and increment
            if left[l] <= right[r]:
                _sorted.append(left[l])
                l += 1
            else:
                _sorted.append(right[r])
                r += 1

        # We are at the end of the left list, add rights
        elif l == n_left:
            _sorted.append(right[r])
            r += 1

        # We are at the end of the right list, add lefts
        elif r == n_right:
            _sorted.append(left[l])
            l += 1

    return _sorted


def merge_sort(values: List[float]) -> List[float]:
    """
    Sequentially split lists into ordered pairs, then merges
    the results
    """
    n = len(values)

    # Exit early on n == 1, when all possible splits have 
    # been done
    if n == 1:
        return values

    # Index of integer midpoint
    i_mid = len(values) // 2

    left: List[float] = merge_sort(values[:i_mid])
    right: List[float] = merge_sort(values[i_mid:])

    return _merge(left, right)