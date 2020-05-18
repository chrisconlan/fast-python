def naive_in_operator(value: str, 
    sequence: List[str]) -> bool:
    """
    Check if a value is in the sequence, naively

    This is O(n) for sequence of length n
    """
    is_in = False
    for other_value in sequence:
        if value == other_value:
            is_in = True
    return is_in