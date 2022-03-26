# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import base64
from fileinput import filename
import hashlib
from urllib.parse import urlparse
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class CustomHtmlDownloaderMiddleware:
    def process_response(self, request, response, spider):
        url_hash = hashlib.md5(response.url.encode("utf8")).hexdigest()
        with open(f'out/html/{url_hash}.html', 'wb') as html_file:
            html_file.write(response.body)
        return response


class CustomScreenshotDownloaderMiddleware:
    def process_response(self, request, response, spider):
        url_hash = hashlib.md5(response.url.encode("utf8")).hexdigest()
        if response.data['png']:
            imgdata = base64.b64decode(response.data['png'])
            with open(f'out/screenshots/{url_hash}.png', 'wb') as png_file:
                png_file.write(imgdata)
        return response
