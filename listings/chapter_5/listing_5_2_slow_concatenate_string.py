def slow_concatenate_words(the_words: List[str]) -> str:
    """
    Concatenate a list of strings. This has O(mn^2) memory 
    complexity for n words with an average length of m.
    """
    result: str = ''
    for word in the_words:
        result += word
    return result