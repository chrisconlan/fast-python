def itertuples_loop_df(df: pd.DataFrame):
    """
    .itertuples doesn't allow named-based indexing of 
    closures, but it does allow range-based indexing, so 
    we map each column to its range-based position 
    beforehand.
    """
    last_column = df.columns.values[-1]
    
    # Use i+1 because row[0] is the index
    col_index_by_name = {
        col: i+1 for i, col in enumerate(df.columns.values)
    }
    
    for row in df.itertuples():
        # Row is type pd.core.frame.Pandas,
        # which appears to be a private object
        # similar to a collections.namedtuple
        val = row[col_index_by_name[last_column]]