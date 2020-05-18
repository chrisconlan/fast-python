def re_findall_count(data: str, value: str) -> int:
    """
    Count the number of elements returned in an exhaustive 
    regex search of value on data
    """
    return len(re.findall(value, data))