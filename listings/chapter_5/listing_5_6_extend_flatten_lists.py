def extend_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via extend
    """
    result: List[str] = []
    for _list in the_lists:
        result.extend(_list)
    return result