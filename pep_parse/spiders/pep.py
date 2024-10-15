import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css('table a::attr(href)').getall()
        for link in pep_links:
            yield response.follow(link, self.parse_pep)

    def parse_pep(self, response):
        number = response.css('h1.page-title::text').get().strip().split()[1]
        name = response.css(
            'h1.page-title::text').get().split('–', 1)[1].strip()
        status = response.css('abbr::text').get()
        yield PepParseItem(number=number, name=name, status=status)
