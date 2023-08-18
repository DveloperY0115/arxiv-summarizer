"""
extract_keyword.py

A script for populating the column 'keyword' by analyzing
the column 'abstract' of the given CSV file.
"""

from dataclasses import dataclass, field

import openai
import pandas
import tyro
from tqdm import tqdm


@dataclass
class Args:
    
    openai_api_key: str
    """The private key required to use OpenAI Python API"""
    in_csv: str = field(default_factory=lambda: "./crawler/papers.csv")
    """The path to the CSV file holding the metadata of the papers"""
    gpt_model: str = field(default_factory=lambda: "gpt-3.5-turbo")
    """The name of GPT model to use for keyword extraction"""

def main(args: Args):
    
    raise NotImplementedError("Not tested yet")

    # parse arguments
    csv_file = args.in_csv
    openai_api_key = args.openai_api_key
    gpt_model = args.gpt_model

    # read CSV
    dataframe = pandas.read_csv(csv_file)

    # register API key
    openai.api_key = openai_api_key

    # extract keyword from each abstract
    for row_index, row in tqdm(dataframe.iterrows()):
        title = row["title"]
        abstract = row["abstract"]

        response = openai.ChatCompletion.create(
            model=gpt_model,
            messages=[
                {
                    "role": "system", "content": "You are a helpful assistant.",
                    "role": "user", "content": f"Summarize the following in one sentence: {abstract}",
                }
            ],
            temperature=0.5,
            max_tokens=256
        )

        tldr = response["choices"][0]["message"]["content"]
        print(f"{row_index}: {tldr}")


if __name__ == "__main__":
    args = tyro.cli(Args)
    main(args)
