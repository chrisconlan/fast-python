def np_fast_count(
    the_words: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    This algorithm is O(n) for n words
    """
    return np.unique(the_words, return_counts=True)