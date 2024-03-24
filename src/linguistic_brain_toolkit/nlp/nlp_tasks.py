from typing import List

import pandas as pd
import spacy

def check_text_validity(text: str) -> bool:
    """
    Verifies if the given text is valid for processing with spaCy.

    Args:
    text (str): The text to be verified.

    Returns:
    bool: True if the text is valid, False otherwise.
    """
    return bool(text.strip())  # Check if the text is not empty after stripping whitespace

def lemmatize_word(word_to_lemmatize: str, nlp_model: spacy.language.Language) -> str:
    """
    Lemmatizes the given word using the specified spaCy model.

    Args:
    word_to_lemmatize (str): The word to lemmatize.
    nlp_model (spacy.language.Language): The spaCy model to use for lemmatization.

    Returns:
    str: The lemmatized word.
    """
    doc = nlp_model(word_to_lemmatize)
    lemma = doc[0].lemma_ if len(doc) > 0 else ''  # Lemmatize the word if tokens exist
    return lemma

def pos_tag_word(word_to_tag: str, nlp_model: spacy.language.Language) -> List[str]:
    """
    Performs POS tagging on the given word using the specified spaCy model.
    Returns a list of POS tags.

    Args:
    word_to_tag (str): The word to perform POS tagging on.
    nlp_model (spacy.language.Language): The spaCy model to use for POS tagging.

    Returns:
    List[str]: List of POS tags for the word.
    """
    doc = nlp_model(word_to_tag)
    pos_tags = [token.pos_ for token in doc]  # Get the POS tags
    return pos_tags

def apply_lemmatization_and_pos_tags(data_frame: pd.DataFrame, text_column: str, model_size: str) -> pd.DataFrame:
    """
    Applies lemmatization and POS tagging functions to a DataFrame column using the specified spaCy model size.

    Args:
    data_frame (pd.DataFrame): The DataFrame containing text data.
    text_column (str): The name of the column containing text data.
    model_size (str): The size of the spaCy model to use ('small', 'medium', 'large').

    Returns:
    pd.DataFrame: The DataFrame with added columns for lemmatized words and POS tags.
    """
    # Load the spaCy model based on the specified size
    if model_size == 'small':
        nlp = spacy.load('en_core_web_sm')
    elif model_size == 'medium':
        nlp = spacy.load('en_core_web_md')
    elif model_size == 'large':
        nlp = spacy.load('en_core_web_lg')
    else:
        raise ValueError("Invalid model size. Choose from 'small', 'medium', or 'large'.")

    # Apply the functions to the specified text column using the loaded model
    data_frame['lemmatized_text'] = data_frame[text_column].apply(
        lambda x: lemmatize_word(x, nlp) if check_text_validity(x) else ''
        )
    data_frame['pos_tags'] = data_frame[text_column].apply(
        lambda x: pos_tag_word(x, nlp) if check_text_validity(x) else []
        )

    # Create new columns for each POS tag
    max_pos_tags = data_frame['pos_tags'].apply(len).max()
    for i in range(max_pos_tags):
        data_frame[f'pos_tag_{i+1}'] = data_frame['pos_tags'].apply(
            lambda tags: tags[i] if i < len(tags) else None
            )

    return data_frame
