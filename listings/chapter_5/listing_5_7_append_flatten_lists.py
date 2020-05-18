def append_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via nested append
    """
    result: List[str] = []
    for _list in the_lists:
        for val in _list:
            result.append(val)
    return result