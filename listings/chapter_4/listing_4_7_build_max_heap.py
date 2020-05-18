def _heapify(values: List[float], heap_size: int, 
    root_node: int):
    """
    The ubiquitous heapify function that handles both heap 
    construction and root extraction on a list-based heap, 
    where the children of element i are located at 
    2*i+1 and 2*i+2. 
    """
    n = heap_size

    # Index of the root
    i = root_node

    # Default index of the largest value
    j = root_node

    # Probe these elements as potential roots
    l = 2 * i + 1 # Index of left child node
    r = 2 * i + 2 # Index of right child node

    # Set j to the largest value of a child
    if l < n and values[l] > values[i]:
        j = l

    if r < n and values[r] > values[j]:
        j = r

    # If the root is not the max, set a new root and send 
    # it back through
    if j != i:
        # Swap max and root elements
        values[i], values[j] = values[j], values[i]

        # Recurse
        _heapify(values, n, j)
        
        
def build_max_heap(values: List[float]) -> List[float]:
    """
    Converts values into a max heap.
    """
    n = len(values)

    # Create a max-heap from values
    for i in range(n, -1, -1):
        _heapify(values, n, i)

    # Return a reference to values
    return values