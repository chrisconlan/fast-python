def np_naive_count_lines(filepath):
    """
    Counts lines by parsing file into a numpy array
    """
    data = np.genfromtxt(
        filepath, 
        delimiter=',', 
        skip_header=True
    )
    return data.shape[0]