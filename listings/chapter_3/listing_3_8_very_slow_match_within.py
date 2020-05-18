def very_slow_match_within(first_list: List[str], 
    second_list: List[str]) -> Set[str]:
    """
    This algorithm is O(nm) for n total words in the first 
    list and m total words in the second list
    """
    words = set()
    for word in first_list:
        if word in second_list:
            words.add(word)

    return words