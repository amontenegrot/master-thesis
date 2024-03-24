from linguistic_brain_toolkit.utilities import get_path
from linguistic_brain_toolkit.data import load_dataframes_to_db


PATH = get_path(0)
TEXTGRIDS_FOLDER = PATH + 'data/ds003020/derivative/TextGrids/'
DATABASE_FOLDER = PATH + 'data/processed/transcriptions.db'

load_dataframes_to_db(TEXTGRIDS_FOLDER, DATABASE_FOLDER)
