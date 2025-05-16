import pandas as pd

from typing import Any, Dict, List

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel


class LLMParallelProcessor:
    """Processor that executes LLM queries in parallel on batches of data.

    This processor takes an LLM model and applies it to batches of data contained
    in a DataFrame, replacing in each prompt a placeholder with the corresponding data
    and storing the responses in the DataFrame.
    """

    def __init__(self, llm: Any, batch_size: int) -> None:
        """Initializes the LLMParallelProcessor.

        Args:
            llm (Any): The language model to use for processing requests.
            batch_size (int): The number of rows to process in each batch.
        """
        self.llm = llm
        self.batch_size = batch_size

    def process_batches(
            self,
            df: pd.DataFrame,
            data_column: str,
            prompt_column: str,
            result_column: str,
            data_placeholder: str) -> None:
        """Processes a DataFrame in batches, executing prompts in parallel.

        For each batch of the DataFrame, the specified placeholder in each prompt is
        replaced with the corresponding data, processing chains are generated using the
        LLM model, and the responses are stored in the DataFrame. If there are duplicate
        values in the data column, the response from the last processing in the batch prevails.

        Args:
            df (pd.DataFrame): DataFrame containing the data and prompt templates.
            data_column (str): Name of the column that contains the data to be inserted.
            prompt_column (str): Name of the column that contains the prompt templates.
            result_column (str): Name of the column where the responses will be stored.
            data_placeholder (str): Placeholder in the prompt template to be replaced with the data.
        """
        if result_column not in df.columns:
            df[result_column] = None

        for i in range(0, len(df), self.batch_size):
            batch_data = df[data_column][i:i + self.batch_size].tolist()
            batch_prompts = df[prompt_column][i:i + self.batch_size].tolist()

            # Create formatted prompts by replacing the placeholder with the corresponding data.
            formatted_prompts = [
                prompt.replace(f'{{{data_placeholder}}}', data)
                for data, prompt in zip(batch_data, batch_prompts)
            ]

            # Dynamically create chains and assign them to the LLM model.
            chains = {
                f'response_{idx + 1}': ChatPromptTemplate.from_template(formatted_prompt) | self.llm
                for idx, formatted_prompt in enumerate(formatted_prompts)
            }

            # Execute the chains in parallel.
            map_chain = RunnableParallel(**chains)
            responses = map_chain.invoke({})

            # Build a mapping dictionary for non-null batch data.
            mapping = {
                data: responses[f'response_{idx + 1}']
                for idx, data in enumerate(batch_data) if data is not None
            }

            # Update the DataFrame in a vectorized manner for all rows whose 'data_column'
            # value matches any key in 'mapping'. In case of duplicates, the last result is assigned.
            if mapping:
                mask = df[data_column].isin(mapping.keys())
                df.loc[mask, result_column] = df.loc[mask, data_column].map(mapping)


def semi_format_prompt(
        row: pd.Series,
        prompt_template: str,
        excluded_variables: List[str],
        **variable_values: List[str]
) -> str:
    """Partially formats a prompt by substituting specific variables.

    This function replaces in the prompt template the variables whose names
    are not included in the excluded_variables list, using the provided values
    via keyword arguments.

    Args:
        row (pd.Series): Data row (not directly used in this function).
        prompt_template (str): The prompt template containing placeholders.
        excluded_variables (List[str]): List of variable names that should not be replaced.
        **variable_values (List[str]): Values to substitute in the prompt, associated with their variable names.

    Returns:
        str: The partially formatted prompt with the substitutions applied.

    Raises:
        ValueError: If the prompt template is empty.
    """
    if not prompt_template:
        raise ValueError('The prompt template cannot be empty.')
    
    partially_formatted_prompt = prompt_template

    # Iterate over the provided variables and substitute them if they are not excluded.
    for variable_name, variable_value in variable_values.items():
        if variable_name not in excluded_variables:
            partially_formatted_prompt = partially_formatted_prompt.replace(
                f'{{{variable_name}}}', str(variable_value)
            )
    return partially_formatted_prompt
