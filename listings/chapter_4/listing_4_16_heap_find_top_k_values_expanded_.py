import heapq

def heap_find_top_k_expanded(values: List[float], 
    k: int=20) -> List[float]:
    """
    Given a list of values, convert it into a heap in-place,
    then extract the  top k values from the heap. This is 
    O(n + k*log(n))
    """
    _heap: List[float] = []
    for v in values:
        heapq.heappush(_heap, -v)

    top_k: List[float] = []
    for i in range(k):
        top_k.append(-heapq.heappop(_heap))

    return top_k