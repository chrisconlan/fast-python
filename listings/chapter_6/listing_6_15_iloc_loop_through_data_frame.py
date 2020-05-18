def iloc_loop_df(df: pd.DataFrame):
    """
    Use the a range-based index to look up the row at each
    step, side-stepping the index. This should skip a 
    hashing operation and be faster than the index lookup.
    """
    last_column = df.columns.values[-1]
    for i in range(df.shape[0]):
        row: pd.Series = df.iloc[i]
        val = row[last_column]