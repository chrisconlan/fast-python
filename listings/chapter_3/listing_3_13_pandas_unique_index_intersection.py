def pd_unique_index_match(first_list: List[str], 
    second_list: List[str]) -> List[str]:
    """
    This algorithm is O(n + m) for n words in the first 
    list and m words in the second list

    This is to show that pandas indexes are dict-like, 
    and performance increases for unique elements
    """

    # Create a pandas index from unique elements
    index: pd.Index = pd.Index(set(first_list))

    words: List[str] = []
    for word in set(second_list):
        if word in index:
            words.append(word)

    return words