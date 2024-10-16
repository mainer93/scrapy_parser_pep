import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    domain = 'peps.python.org'
    allowed_domains = [domain]
    start_urls = [f'https://{domain}/']

    def parse(self, response):
        pep_links = response.css('table a::attr(href)').getall()
        for link in pep_links:
            yield response.follow(link, self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('h1.page-title::text').get().strip()
        number, name = page_title.split('–', 1)
        number = number.replace('PEP', '').strip()
        status = response.css('abbr::text').get()
        yield PepParseItem(number=number, name=name.strip(), status=status)
