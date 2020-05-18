def fast_count_lines(filepath):
    """
    Counts lines by iterating through the file directly from
    the disk, reading each line in one at a time
    """
    with open(filepath, 'r') as file_ptr:
        line_count = 0
        for line in file_ptr:
            line_count += 1

    return line_count