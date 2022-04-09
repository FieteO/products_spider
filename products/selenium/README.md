# Selenium script to obtain screenshots
Since scrapy splash is not properly rendering all pages, here we are resorting to Selenium.
The wait time of 2 to 3 seconds in between requests is large enough to fully load most pages.

## Required Firefox extensions
Ublock Origin and and I don't care about cookies are used to avoid ads and cookie consent popups in the screenshots.
To download them, head to the respective addon page ([uBlock](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search), [IDCAC](https://addons.mozilla.org/en-US/firefox/addon/i-dont-care-about-cookies/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)) and copy the link of the `Add to Firefox` button. Then download the file, for example with
``` bash
(spider)fiete@ubu:~/Documents/studium/bdp/spider/products/selenium$ wget https://addons.mozilla.org/firefox/downloads/file/3933192/ublock_origin-1.42.4-an+fx.xpi
```