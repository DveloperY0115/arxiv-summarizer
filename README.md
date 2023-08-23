# arxiv-summarizer

## How to Use

Create a Python virtual environment by issuing the command:
```
conda create -f environment.yaml
```

# How to use Crawler

To crawl the abstract texts from one or more arXiv pages, 
1. Populate the list `start_urls` in `crawler/crawler/spiders/arxiv.py` with the URLs of paper abstract pages (e.g., "https://arxiv.org/abs/2102.09105")
2. Change the current working directory to `crawler` and issue the command `scrapy crawl Arxiv -o papers.csv -t csv`
3. The output CSV file will be stored under the current working directory.

# How to use Summarizer

Having created a CSV file holding the title and abstract of the paper crawled from arXiv, you can now use the summarizer to generate a summary of each paper. 

Before that, visit the [GitHub repository of Llama2](https://github.com/facebookresearch/llama) and follow the instruction to setup Llama.
**You may need to install PyTorch to your virtual environment in advance.**

Then, issue the command:
```
torchrun --nproc_per_node 1 summarizer/summarize_abstract.py --in_csv {PATH_TO_CSV_FILE}
```