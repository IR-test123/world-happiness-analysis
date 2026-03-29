from pathlib import Path
import pandas as pd

def write_df_to_csv(df: pd.DataFrame, folder_path: str) -> None:
    path = Path(folder_path)
    df.to_csv(path, index=False)