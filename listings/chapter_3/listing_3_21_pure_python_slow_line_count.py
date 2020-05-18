def slow_count_lines(filepath):
    """
    Counts lines by reading entire file into memory as a 
    list of lines represented by strings
    """
    with open(filepath, 'r') as file_ptr:
        lines: List[str] = file_ptr.readlines()
        line_count = len(lines)
    return line_count