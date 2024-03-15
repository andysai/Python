import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
label = driver.find_element_by_class_name('teacher')
print(label.get_attribute('type'))
driver.close()