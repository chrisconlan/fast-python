def pd_fast_count(
    the_words: pd.Series) -> pd.Series:
    """
    This algorithm is O(n) for n words
    """
    return the_words.value_counts()