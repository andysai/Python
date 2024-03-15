import time

from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
print(dir(driver.find_element))
teacher = driver.find_element_by_class_name('teacher')
teacher.send_keys('吴枫')
assistant = driver.find_element_by_class_name('assistant')
assistant.send_keys('都喜欢')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(1)
driver.close()