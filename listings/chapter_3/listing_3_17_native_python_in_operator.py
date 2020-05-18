def native_in_operator(value: str,
    sequence: List[str]) -> bool:
    """
    Use Python's native in operator to check if a value is 
    in a sequence

    This is O(n) for sequence of length n
    """
    return value in sequence