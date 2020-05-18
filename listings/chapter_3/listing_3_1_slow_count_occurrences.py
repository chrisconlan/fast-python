def slow_count_occurrences(
    the_words: List[str]) -> List[Tuple[str, int]]:
    """
    This algorithm is O(nm) for n total words and m unique 
    words
    """

    # Our output data structure will be a list of tuples
    count_by_word = list()

    # Get a list of all unique words using set
    unique_words = set(the_words)

    # Loop through unique words
    for word_a in unique_words:

        # Count the occurences
        accumulator = 0
        for word_b in the_words:
            if word_a == word_b:
                accumulator += 1

        # Store the character with the count
        count_by_word.append((word_a, accumulator))

    return count_by_word