def slow_add_flatten_lists(
    the_lists: List[List[str]]) -> List[str]:
    """
    Flatten a list of lists via list addition. This has 
    O(mn^2) compexity for n lists with average length m
    """
    result: List[str] = []
    for _list in the_lists:
        result = result + _list
    return result