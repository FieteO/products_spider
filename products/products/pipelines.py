# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import base64
from itemadapter import ItemAdapter
import hashlib
from urllib.parse import quote

import scrapy
from itemadapter import ItemAdapter
from scrapy.utils.defer import maybe_deferred_to_future
from scrapy_splash import SplashRequest


class ProductsPipeline:
    def process_item(self, item, spider):
        return item


# https://docs.scrapy.org/en/latest/topics/item-pipeline.html#take-screenshot-of-item
class ScreenshotPipeline:
    """Pipeline that uses Splash to render screenshot of
    every Scrapy item."""

    SPLASH_URL = "http://localhost:8050/render.png?url={}"

    async def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        encoded_item_url = quote(adapter["url"])
        screenshot_url = self.SPLASH_URL.format(encoded_item_url)
        request = SplashRequest(screenshot_url, args={'png':1})
        # request = scrapy.Request(screenshot_url)
        response = await maybe_deferred_to_future(spider.crawler.engine.download(request, spider))

        if response.status != 200:
            # Error happened, return item.
            return item

        # Save screenshot to file, filename will be hash of url.
        url = adapter["url"]
        url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
        filename = f"out/images/{adapter['hostname']}_{url_hash}.png"

        imgdata = base64.b64decode(response.data['png'])

        with open(filename, "wb") as f:
            f.write(imgdata)

        # Store filename in item.
        adapter["screenshot_filename"] = filename
        return item