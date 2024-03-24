import os
import sqlite3
from typing import Tuple

import pandas as pd
import numpy as np
import textgrid


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

def create_table_if_not_exists(cursor, df_temp):
    """
    Create a table in the database if it does not exist.

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor.
    df_temp (pd.DataFrame): The DataFrame used to determine the table structure.

    Returns:
    None
    """
    if not cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='general';").fetchone():
        cols = ', '.join(f'"{col}" {dtype}' for col, dtype in zip(df_temp.columns, df_temp.dtypes.replace({np.dtype('O'): 'TEXT', np.dtype('int64'): 'INTEGER', np.dtype('float64'): 'REAL'})))
        cursor.execute(f'CREATE TABLE general ({cols});')

def load_dataframes_to_db(folder_path: str, db_path: str) -> None:
    """
    Load all valid TextGrid files in a folder into a SQLite database.
    If the database does not exist, it will be created.

    Parameters:
    folder_path (str): The path to the folder containing the files.
    db_path (str): The path to the SQLite database.

    Returns:
    None
    """
    valid_files, _ = check_textgrid_files(folder_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for file in valid_files:
        file_path = os.path.join(folder_path, file)
        df_name = os.path.splitext(file)[0]
        df_temp = load_single_dataframe(file_path, df_name)
        create_table_if_not_exists(cursor, df_temp)
        df_temp.to_sql('general', conn, if_exists='append', index=False)
        print(f'DataFrame from {df_name} loaded into database.')
        del df_temp
    conn.close()
