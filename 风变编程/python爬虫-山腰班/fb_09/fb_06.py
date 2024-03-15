import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
labels = driver.find_elements_by_tag_name('label')
for label in labels:
    print(label.text)
driver.close()
