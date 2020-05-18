def index_loop_df(df: pd.DataFrame):
    """
    Use the pandas index to look up the row at each step. 
    pandas indexes are dict-like, so the lookup in O(1).
    """
    last_column = df.columns.values[-1]
    for i in df.index:
        row: pd.Series = df.loc[i]
        val = row[last_column]
