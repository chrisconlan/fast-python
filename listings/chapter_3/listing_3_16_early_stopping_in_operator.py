def early_stopping_in_operator(value: str, 
    sequence: List[str]) -> bool:
    """
    Check if a value is in the sequence with early stopping

    This is O(n) for sequence of length n
    """
    for other_value in sequence:
        if value == other_value:
            return True
    return False