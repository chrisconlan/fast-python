def pd_naive_index_match(first_list: List[str], 
    second_list: List[str]) -> List[str]:
    """
    This algorithm is O(n + m) for n words in the first 
    list and m words in the second list

    This is to show that pandas indexes are dict-like 
    even when the elements are not unique
    """

    # Create a pandas index of of the list as-is
    index: pd.Index = pd.Index(first_list)

    words: List[str] = []
    for word in set(second_list):
        if word in index:
            words.append(word)

    return words