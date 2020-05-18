def loop_build_dict(words: List[str]) -> Dict[str, str]:
    """
    Build a dictionary by looping through each element of 
    the list and declaring it as the key-value pair
    """
    result = dict()
    for word in words:
        result[word] = word
    return result
    
def list_build_dict(
    words: List[str]) -> Dict[str, str]:
    """
    Build a dictionary by passing a list of tuples to the 
    dict constructor
    """
    return dict([(w, w) for w in words])

def generator_build_dict(
    words: List[str]) -> Dict[str, str]:
    """
    Build a dictionary by passing a generator of tuples to 
    the dict constructor
    """
    return dict(((w, w) for w in words))
    
def comprehension_build_dict(
    words: List[str]) -> Dict[str, str]:
    """
    Build a dictionary using a dict comprehension
    """
    return {w: w for w in words}