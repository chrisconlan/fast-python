import heapq

def heap_find_top_k(values: List[float], 
    k: int=20) -> List[float]:
    """
    Given a list of values, convert it into a heap in-place,
    then extract the top k values from the heap. This is 
    O(n + k*log(n))
    """
    return heapq.nlargest(k, values)