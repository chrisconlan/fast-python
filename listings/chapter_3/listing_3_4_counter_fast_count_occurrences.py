from collections import Counter

def counter_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    """
    This algorithm is O(n) for n words
    """
    return Counter(the_words)