def fast_intersection(first_list: List[str], 
    second_list: List[str]) -> Set[str]:
    """
    This algorithm is O(n + m) for n words in the first 
    list and m words in the second list.

    This problem boils down to a set intersection.
    """
    return set(first_list) & set(second_list)