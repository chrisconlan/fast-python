def str_split_count(data: str, value: str) -> int:
    """
    Return the number of occurrences of value in data by 
    splitting data along value into a list
    """
    return len(data.split(value)) - 1