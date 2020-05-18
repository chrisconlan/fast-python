def pd_naive_count_lines(filepath):
    """
    Counts lines by parsing file into a pd.DataFrame
    """
    df = pd.read_csv(filepath)
    return df.shape[0]