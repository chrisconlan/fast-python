def slow_match_within(first_list: List[str], 
    second_list: List[str]) -> List[str]:
    """
    This algorithm is O(nm) for n unique words in the first 
    list and m total words in the second list
    """

    # Get the unique words
    unique_words = set(first_list)

    words = list()
    for word in unique_words:
        if word in second_list:
            words.append(word)

    return words