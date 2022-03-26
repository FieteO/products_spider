# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class ProductsItem(scrapy.Item):
    url = Field()
    hostname = Field()
    screenshot_filename = Field()
    html_filename = Field()
    html = Field()
