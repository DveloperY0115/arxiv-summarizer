"""
summarize_abstract.py

A script for populating the column 'keyword' and 'tldr' by analyzing
the column 'abstract' of the given CSV file using LLMs.
"""

from typing import Optional

import fire
from llama import Llama
import pandas
import tyro
from tqdm import tqdm
    

def parse_keyword_from_response(result) -> str:
    """Parses the keyword from Llama responses."""
    
    role: str = result["generation"]["role"]
    assert role.lower() == "assistant", f"Unexpected role: {role}"
    generated_lines = result["generation"]["content"].splitlines()

    # exclude the starting line from the assistant
    generated_lines = generated_lines[1:]
    
    # clean up the individual line
    keywords = []

    try:
        for line in generated_lines:
            line_clean = line.split(".")[1].strip().lower()
            if ":" in line_clean:
                line_clean = line_clean.split(":")[0].strip()
            keywords.append(line_clean)
    except:
        keywords = generated_lines

    # compile the lines into one paragraph
    keywords = ", ".join(keywords)

    return keywords

def main(
    in_csv: str = "./crawler/papers.csv",
    llama_ckpt_dir: str = "./externals/llama/data/pretrained_models/llama-2-7b-chat/",
    tokenizer_path: str = "./externals/llama/data/pretrained_models/tokenizer.model",
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 8192,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,  
):
    """
    Extracts keywords from the texts provided via the CSV file using LLMs.
    
    Args:
        in_csv: The path to the CSV file holding the metadata of the papers
        llama_ckpt_dir: The path to the Llama 2 checkpoint directory
        tokenizer_path: The path to the tokenizer model
        temperature:
        top_p:
        max_seq_len: The maximum sequence length of the input to the LLMs
        max_gen_len: The maximum length of the generated text
        max_batch_size: The maximum batch size of the LLMs
    """    

    # read CSV
    dataframe = pandas.read_csv(in_csv)

    # build model
    generator = Llama.build(
        ckpt_dir=llama_ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    # extract keyword from each abstract
    num_row = dataframe.shape[0]
    for row_index, row in tqdm(dataframe.iterrows(), total=num_row):

        # get abstract to summarize
        abstract = row["abstract"]

        # populate dialog
        dialogs = [
            [
                {
                    "role": "system",
                    "content": """\
                        You are a professional scholar in computer vision. Always answer as concisely as possible, while being accurate.
                    """
                },
                {
                    "role": "user",
                    "content": f"Extract five most important keywords from the following text as a bullet list: {abstract}",
                },
            ],
        ]

        # query Llama
        results = generator.chat_completion(
            dialogs,  # type: ignore
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=top_p,
        )

        # update dataframe
        for result in results:
            keywords = parse_keyword_from_response(result)
            dataframe.at[row_index, "keywords"] = keywords

    # save dataframe
    dataframe.to_csv(in_csv, index=False)

if __name__ == "__main__":
    fire.Fire(main)
