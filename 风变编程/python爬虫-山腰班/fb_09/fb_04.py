from selenium.webdriver.chrome.webdriver import RemoteWebDriver
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities())
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
label = driver.find_element_by_tag_name('label')
print(label.text)
driver.close()
