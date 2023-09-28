import pandas as pd

def explore_dataframe(df):
    """Explore a Pandas DataFrame

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to explore

    Returns
    -------
    None
    """
    # Exploring first and last rows of df
    print("First 5 rows:")
    print(df.head())
    print("\nLast 5 rows:")
    print(df.tail())

    # Shape of df
    print("\nShape of DataFrame:", df.shape)

    # Displaying column names
    print("\nColumn Names:")
    print(df.columns.tolist())
