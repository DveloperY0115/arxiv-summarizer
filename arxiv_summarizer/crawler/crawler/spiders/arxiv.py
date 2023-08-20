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
        "https://arxiv.org/abs/1711.07566",
        "https://arxiv.org/abs/1812.01024",
        "https://arxiv.org/abs/1904.01786",
        "https://arxiv.org/abs/2010.07492",
        "https://arxiv.org/abs/2011.13961",
        "https://arxiv.org/abs/2003.08934",
        "https://arxiv.org/abs/2008.05511",
        "https://arxiv.org/abs/2004.03805",
        "https://arxiv.org/abs/2003.09852",
        "https://arxiv.org/abs/2007.02442",
        "https://arxiv.org/abs/2112.05504",
        "https://arxiv.org/abs/2111.14643",
        "https://arxiv.org/abs/2112.07945",
        "https://arxiv.org/abs/2102.07064",
        "https://arxiv.org/abs/2112.05131",
        "https://arxiv.org/abs/2112.07945",
        "https://arxiv.org/abs/2008.02268",
        "https://arxiv.org/abs/2103.05606",
        "https://arxiv.org/abs/2103.00762",
        "https://arxiv.org/abs/2012.02190",
        "https://arxiv.org/abs/2011.07233",
        "https://arxiv.org/abs/2012.00926",
        "https://arxiv.org/abs/2011.12100",
        "https://arxiv.org/abs/2012.03927",
        "https://arxiv.org/abs/2103.13744",
        "https://arxiv.org/abs/2103.10380",
        "https://arxiv.org/abs/2104.06405",
        "https://arxiv.org/abs/2012.03918",
        "https://arxiv.org/abs/2011.12948",
        "https://arxiv.org/abs/2103.13415",
        "https://arxiv.org/abs/2104.00677",
        "https://arxiv.org/abs/2012.12247",
        "https://arxiv.org/abs/2103.14024",
        "https://arxiv.org/abs/2109.01847",
        "https://arxiv.org/abs/2102.08860",
        "https://arxiv.org/abs/2110.07604",
        "https://arxiv.org/abs/2106.12052",
        "https://arxiv.org/abs/2106.10689",
        "https://arxiv.org/abs/2011.10379",
        "https://arxiv.org/abs/2106.13228",
        "https://arxiv.org/abs/2202.05263",
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
