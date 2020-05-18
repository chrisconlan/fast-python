def fast_match_within(first_list: List[str], 
    second_list: List[str]) -> List[str]:
    """
    This algorithm is O(n + m) for n unique words in the 
    first list and m total words in the second list
    """

    # Get the unique words
    first_list_unique_words = set(first_list)
    second_list_unique_words = set(second_list)

    words = list()
    for word in first_list_unique_words:
        if word in second_list_unique_words:
            words.append(word)

    return words