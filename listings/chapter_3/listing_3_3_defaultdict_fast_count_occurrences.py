from collections import defaultdict

def defaultdict_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    """
    This algorithm is O(n) for n words
    """

    # A dictionary whose values default to zero
    count_by_word = defaultdict(int)

    # Loop through the words
    for word in the_words:

        # Incriment the counter
        count_by_word[word] += 1

    return count_by_word