def fast_count_occurrences(
    the_words: List[str]) -> Dict[str, int]:
    """
    This algorithm is O(n) for n words
    """

    # Our output data structure
    count_by_word = dict()

    # Loop through the words
    for word in the_words:

        # Make sure the dictionary knows about the words
        if not word in count_by_word:
            count_by_word[word] = 0

        # Incriment the counter
        count_by_word[word] += 1

    return count_by_word