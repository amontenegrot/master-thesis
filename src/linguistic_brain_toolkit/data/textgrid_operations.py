import os
from typing import Tuple

import pandas as pd
import textgrid

from .sqlite_operations import load_dataframe_to_sqlite


def check_textgrid_files(folder_path: str) -> tuple:
    """
    Check all TextGrid files in a folder.

    Parameters:
    folder_path (str): The path to the folder containing the files.

    Returns:
    tuple: Two lists, the first one contains the names of the valid TextGrid files,
           the second one contains the names of the invalid TextGrid files.
    """
    valid_files = []
    invalid_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.TextGrid'):
            file_path = os.path.join(folder_path, file)
            if is_valid_textgrid(file_path):
                valid_files.append(file)
            else:
                invalid_files.append(file)
    return valid_files, invalid_files

def is_valid_textgrid(file_path: str) -> bool:
    """
    Check if a file is a valid TextGrid file.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    bool: True if the file is a valid TextGrid file, False otherwise.
    """
    with open(file_path, 'r') as f:
        first_line = f.readline().strip()
        second_line = f.readline().strip()
        third_line = f.readline().strip()
        fourth_line = f.readline().strip()
    return (first_line == 'File type = "ooTextFile"' and 
            second_line == 'Object class = "TextGrid"' and 
            third_line == '' and
            fourth_line.startswith('xmin = '))

def load_single_dataframe(file_path: str, file_name: str) -> pd.DataFrame:
    """
    Load a single TextGrid file into memory as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the file.
    file_name (str): The name of the file.

    Returns:
    df (pd.DataFrame): The loaded DataFrame.
    """
    tgrid = textgrid.read_textgrid(file_path)
    df = pd.DataFrame(tgrid)
    df['source'] = file_name
    return df

def load_dataframes_to_db(folder_path: str, db_path: str, if_exists='append') -> None:
    """
    Load all valid TextGrid files in a folder into a SQLite database.
    If the database does not exist, it will be created.

    Parameters:
    folder_path (str): The path to the folder containing the files.
    db_path (str): The path to the SQLite database.
    if_exists (str): Action to take if the table already exists. Options are 'fail', 'replace', or 'append'. Defaults to 'append'.

    Returns:
    None
    """
    valid_files, _ = check_textgrid_files(folder_path)
    for file in valid_files:
        file_path = os.path.join(folder_path, file)
        df_name = os.path.splitext(file)[0]
        df_temp = load_single_dataframe(file_path, df_name)
        load_dataframe_to_sqlite(
            df_temp, db_path,
            table_name='general',
            if_exists=if_exists, df_name=df_name
            )
        del df_temp
