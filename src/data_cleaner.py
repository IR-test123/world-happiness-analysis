def normalize_columns(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(r"[.\(\)]", "_", regex=True)   # replace dots & parentheses → underscore
        .str.replace(r"\s+", "_", regex=True)      # spaces → underscore
        .str.replace(r"_+", "_", regex=True)       # collapse multiple _
    )
    return df


def standardize_df(df, file_id, column_mapping):
    df = normalize_columns(df)

    df = df.rename(columns=column_mapping)

    # Keep only relevant columns
    cols_to_keep = [
        "country",
        "rank",
        "happiness_score",
        "gdp_per_capita",
        "social_support",
        "life_expectancy",
        "freedom",
        "generosity",
        "corruption",
        "dystopia_residual"
    ]

    for col in cols_to_keep:
        if col not in df.columns:
            df[col] = None

    df = df[cols_to_keep]

    df["file_id"] = file_id

    return df


