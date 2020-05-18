def medium_count_lines(filepath):
    """
    Counts lines by reading entire file into memory as a 
    string then counting line breaks
    """
    with open(filepath, 'r') as file_ptr:
        file_str: List[str] = file_ptr.read()
        line_count = file_str.count('\n')
    return line_count