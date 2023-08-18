# arxiv-summarizer

## How to Use

Create a Python virtual environment by issuing the command:
```
conda create -f environment.yaml
```

To crawl the abstract texts from one or more arXiv pages, 
1. Populate the list `start_urls` in `crawler/crawler/spiders/arxiv.py` with the URLs of paper abstract pages (e.g., "https://arxiv.org/abs/2102.09105")
2. Save the file and issue the command `scrapy crawl Arxiv -o papers.csv -t csv`
3. The output CSV file will be stored under the current working directory.
