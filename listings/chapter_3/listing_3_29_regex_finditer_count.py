def re_finditer_count(data: str, value: str) -> int:
    """
    Count the number of elements returned in an exhaustive 
    regex search of value on data, as an iterator
    """
    return sum(1 for _ in re.finditer(value, data))