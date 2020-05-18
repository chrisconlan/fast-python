import mmap

def fast_mem_map_count(filename):
    """
    Create a memory-mapping in order to count the lines
    """
    with open(filename, 'r+') as file_ptr:
        memory_map = mmap.mmap(file_ptr.fileno(), 0)
        line_count = 0
        while memory_map.readline():
            line_count += 1
    return line_count