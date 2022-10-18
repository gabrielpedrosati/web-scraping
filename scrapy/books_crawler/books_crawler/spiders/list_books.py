import scrapy


class ListBooksSpider(scrapy.Spider):
    name = 'list_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass
