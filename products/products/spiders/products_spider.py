import hashlib
import pathlib
import scrapy
from scrapy_splash import SplashRequest

from products.items import ProductsItem
from urllib.parse import urlparse


class ProductsSpiderSpider(scrapy.Spider):
    name = 'products_spider'
    allowed_domains = ['ducati.com','citroen.com']
    start_urls = ['https://ducati.com','https://citroen.com']

    def start_requests(self):

        outdir = pathlib.Path('out')
        outdir.mkdir(exist_ok=True)
        outdir.joinpath('html').mkdir(exist_ok=True)
        outdir.joinpath('screenshots').mkdir(exist_ok=True)
        
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.json',
                                args={ 'wait': 2, 'html':1, 'png':1, 'render_all':1 }, magic_response=True)

    def parse(self, response):
        item = ProductsItem()
        url_hash = hashlib.md5(response.url.encode("utf8")).hexdigest()
        item['url']         = response.url
        item['hostname']    = urlparse(response.url).hostname.replace('www.','')
        item['html']        = response.body
        item['html_filename'] = f'out/html/{url_hash}.png'
        item['screenshot_filename'] = f'out/screenshots/{url_hash}.png'
        yield item

        # recursively parse subpages
        links = response.css('a::attr(href)').extract()
        for href in links:
            yield SplashRequest(response.urljoin(href), self.parse, endpoint='render.json',
                                args={ 'wait': 2, 'html':1, 'png':1 }, magic_response=True)
