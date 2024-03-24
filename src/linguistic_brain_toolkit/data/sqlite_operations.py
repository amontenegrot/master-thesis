import sqlite3

# import pandas as pd
import numpy as np


def load_dataframe_to_sqlite(df, db_path, table_name='default', if_exists='append', df_name='df'):
    """
    Load a pandas DataFrame into a SQLite database table.

    Parameters:
    df (pd.DataFrame): The DataFrame to be loaded.
    db_path (str): The path to the SQLite database.
    table_name (str): The name of the table in the database. Defaults to 'general'.
    if_exists (str): Action to take if the table already exists. Options are 'fail', 'replace', or 'append'. Defaults to 'append'.

    Returns:
    None
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cols = ', '.join(f'"{col}" {dtype}' for col, dtype in zip(
            df.columns, df.dtypes.replace(
                {np.dtype('O'): 'TEXT', np.dtype('int64'): 'INTEGER', np.dtype('float64'): 'REAL'}
                )))
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({cols});')
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)
        print(f'DataFrame {df_name} loaded into table {table_name}.')
    except sqlite3.Error as e:
        print(f'An error occurred loading dataframe {df_name} in table {table_name}:\n{e}')
        conn.rollback()  # Roll back any changes if an error occurs
    finally:
        conn.commit()  # Commit changes
        cursor.close()
        conn.close()
