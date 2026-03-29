from pandas import DataFrame

def normalize_columns(df: DataFrame) -> DataFrame:
    '''

    :param df: Original DataFrame
    :return: Modified DataFrame - changed column names to a normalized format
    '''
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(r"[.\(\)]", "_", regex=True)   # replace dots & parentheses → underscore
        .str.replace(r"\s+", "_", regex=True)      # spaces → underscore
        .str.replace(r"_+", "_", regex=True)       # collapse multiple _
    )
    return df

def standardize_df(df: DataFrame, file_id: str, column_mapping: dict, columns_to_keep: list,
                   col_source_row, col_file_id) -> DataFrame:
    '''
    :param df: Original DataFrame
    :param file_id: String representing the file ID - year of data
    :param column_mapping: (Changing column names to crate a standardized format for all years)
    :param columns_to_keep: List of columns to keep - ones that have relevance across all years.
    :param col_source_row: standard name for column of original row index
    :param col_file_id: standard name for file ID column - year of data
    :return: Standardized DataFrame
    '''

    df = df.copy()

    # Save original row index for debugging
    df[col_source_row] = df.index

    df = normalize_columns(df)

    df = df.rename(columns=column_mapping)

    for col in columns_to_keep:
        if col not in df.columns:
            df[col] = None

    df = df[[col_source_row] + columns_to_keep]

    df[col_file_id] = file_id

    return df

