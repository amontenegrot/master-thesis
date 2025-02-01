# import pandas as pd

from linguistic_brain_toolkit.data import read_data_from_database, load_dataframe_to_sqlite
from linguistic_brain_toolkit.nlp import apply_lemmatization_and_pos_tags
from linguistic_brain_toolkit.utilities import get_path


PATH = get_path(0)
DATABASE_FOLDER = PATH + 'data/processed/transcriptions.db'

df = read_data_from_database(DATABASE_FOLDER, 'general')

# Preprocessing
df = df.rename({'name':'orthographic_word'}, axis=1)
df['orthographic_word'] = df['orthographic_word'].str.lower()

df_orthographic_transcription = df.query("tier == 'word'").copy()

# Eliminate non-linguistic sounds: silences, clapping, noises, etc.
strings_to_exclude = ('{', 'sp', 'chuck-e-cheese')  # morphologically complex word
condition = df_orthographic_transcription.astype(str).apply(
    lambda row: row.str.contains('|'.join(strings_to_exclude)
                                 )).any(axis=1)
df_filtered = df_orthographic_transcription[~condition].copy()

# NLP
df_processed = apply_lemmatization_and_pos_tags(
    df_filtered,
    'orthographic_word',
    'large'
    )
del df, df_orthographic_transcription, df_filtered  # Delete dataframes to free memory

cols_to_process = [col for col in df_processed.columns if col.startswith('pos_tag_')]

for col in cols_to_process:
    df_processed[col] = df_processed[col].fillna('')

df_processed.reset_index(drop=True, inplace=True)
df_processed.drop(['pos_tags'], axis=1, inplace=True)

load_dataframe_to_sqlite(
    df_processed,
    DATABASE_FOLDER,
    'nlp_orthographic_transcriptions',
    if_exists='replace',
    df_name='df_processed'
    )
