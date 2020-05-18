def comprehension_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via nested list comprehension
    """
    return [val for _list in the_lists for val in _list]