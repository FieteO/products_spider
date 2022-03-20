import scrapy
from scrapy_splash import SplashRequest

from products.items import ProductsItem


class ProductsSpiderSpider(scrapy.Spider):
    name = 'products_spider'
    allowed_domains = ['example.com']
    start_urls = ['https://ducati.com','https://citroen.com']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.json',
                                args={ 'wait': 1 })

    def parse(self, response):
        print(response)
        item = ProductsItem(
            url = response.url,
            hostname = response.url.replace('http://localhost:8050','')
        )
        yield item
