def python_timsort(values: List[float]):
    values.sort()
    
def numpy_timsort(values: List[float]):
    return np.sort(values, kind='stable')
    
def numpy_quicksort(values: List[float]):
    return np.sort(values, kind='quicksort')
    
def numpy_heapsort(values: List[float]):
    return np.sort(values, kind='heapsort')