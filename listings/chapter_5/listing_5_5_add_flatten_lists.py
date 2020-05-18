def add_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via list addition
    """
    result: List[str] = []
    for _list in the_lists:
        result += _list
    return result