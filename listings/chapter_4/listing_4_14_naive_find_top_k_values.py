def naive_find_top_k(values: List[float], 
    k: int=20) -> List[float]:
    """
    Given a list of values, find the highest k values by 
    sorting the entire list first. This is O(n*log(n))
    """
    values.sort(reverse=True)
    return values[:k]