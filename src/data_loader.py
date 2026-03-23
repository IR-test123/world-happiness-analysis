from pathlib import Path
import pandas as pd

RAW_DATA_PATH = "../data/raw"


def load_all_csvs(folder_path: str) -> dict:
    '''

    :param folder_path: location of csv files
    :return: a dict of consisting of filename(without csv suffix) as key, and data frame of file data as value
    '''
    folder = Path(folder_path)
    dfs = {}

    for file in folder.glob("*.csv"):
        key = file.stem  # e.g. "2015"
        dfs[key] = pd.read_csv(file)

    return dfs


raw_data = load_all_csvs(RAW_DATA_PATH)

print(raw_data)