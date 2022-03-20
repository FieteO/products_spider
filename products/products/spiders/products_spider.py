import scrapy
from scrapy_splash import SplashRequest

from products.items import ProductsItem
from urllib.parse import urlparse


class ProductsSpiderSpider(scrapy.Spider):
    name = 'products_spider'
    allowed_domains = ['example.com']
    start_urls = ['https://ducati.com','https://citroen.com']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.json',
                                args={ 'wait': 1.5 })

    def parse(self, response):
        item = ProductsItem()
        item['url']         = response.url
        raw_url = response.url.replace('http://localhost:8050','')
        item['hostname']    = urlparse(raw_url).hostname.replace('www.','')
        yield item
