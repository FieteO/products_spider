import hashlib
import random
import time
import os
import pandas as pd
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service

# https://www.selenium.dev/documentation/
options = Options()
profile = FirefoxProfile()
# profile.add_extension('uBlock0_1.38.6.firefox.xpi')
# profile.set_preference("browser.privatebrowsing.autostart", True)
options.profile = profile
options.headless = True
service = Service(executable_path='/usr/bin/geckodriver')
driver = webdriver.Firefox(service=service,options=options)

project_path = Path.cwd()
print(project_path)
print(project_path.parent)
driver.install_addon(project_path.joinpath('ublock_origin-1.42.4-an+fx.xpi'))
driver.install_addon(project_path.joinpath('i_dont_care_about_cookies-3.3.8-an+fx.xpi'))

urls = pd.read_csv(project_path.parent.joinpath('in/domains.csv'))['0']
for url in urls:
    driver.get(url)
    url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
    outpath = project_path.parent.joinpath(f'out/screenshots/{url_hash}.png')
    # wait between 0 and 1 seconds to not DoS the websites
    time.sleep(random.uniform(2,3))
    print(outpath)
    driver.save_full_page_screenshot(outpath.as_posix())

