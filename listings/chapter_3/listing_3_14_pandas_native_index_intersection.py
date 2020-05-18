def pd_native_index_match(first_list: List[str], 
    second_list: List[str]) -> pd.Index:
    """
    This algorithm is O(n + m) for n words in the first 
    list and m words in the second list
    """

    # Create a pandas index from unique elements
    first_index = pd.Index(set(first_list))
    second_index = pd.Index(set(second_list))
    return first_index.intersection(second_index)