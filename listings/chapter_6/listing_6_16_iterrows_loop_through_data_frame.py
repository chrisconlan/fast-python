def iterrows_loop_df(df: pd.DataFrame):
    """
    Iterrows is the vanilla and recommended solution for 
    looping through data frames
    """
    last_column = df.columns.values[-1]
    for i, row in df.iterrows():
        # row is a pd.Series
        val = row[last_column]