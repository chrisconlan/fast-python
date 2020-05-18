def fast_concatenate_words(the_words: List[str]) -> str:
    """
    Concatenate a list of strings. This has O(mn) memory 
    complexity for n words with an average length of m.
    """
    return ''.join(the_words)