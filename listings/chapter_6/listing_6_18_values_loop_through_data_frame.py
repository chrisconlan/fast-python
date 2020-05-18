def values_loop_df(df: pd.DataFrame):
    """
    .values converts the data frame to a numpy array before 
    looping, which is fast but no memory-friendly
    """
    last_column = df.columns.values[-1]
    col_index_by_name = {
        col: i for i, col in enumerate(df.columns.values)
    }
    for row in df.values:
        val = row[col_index_by_name[last_column]]