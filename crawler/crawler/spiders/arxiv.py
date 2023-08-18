import datetime
import re
import scrapy


class ArxivSpider(scrapy.Spider):
    name: str = "Arxiv"
    search_term: str = "Graph Neural Networks"
    search_term = search_term.replace(" ", "+")

    # TODO: How to crawl only the given URLs?
    # start_urls = [
    #     f"https://arxiv.org/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term={search_term}&terms-0-field=title&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first"
    # ]
    start_urls = [
        "https://arxiv.org/abs/1912.06395",
        "https://arxiv.org/abs/2201.13168",
        "https://arxiv.org/abs/2102.09105",
        "https://arxiv.org/abs/2203.16529",
    ]

    def parset_out_html(self, string):
        """
        TODO: Add documentation
        """
        string = string.strip().replace("\n", "").strip(' ')
        string = re.sub(r'<[^>]*>', '', string)
        string = string.strip()
        return string
    
    def parse(self, response):
        """
        Parses HTML response from the given URL and extracts the paper title and abstract.
        """
        yield {
            "title": response.xpath("//meta[@name='citation_title']/@content")[0].extract(),
            "abstract": response.xpath("//meta[@name='citation_abstract']/@content")[0].extract(),
        }
