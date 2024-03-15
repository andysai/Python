import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('吴枫')
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('酱酱')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(2)
content = driver.find_element_by_class_name('content')
name = content.find_element_by_tag_name('h1')
message = content.find_element_by_tag_name('p')
print(name.text + '\n' + message.text)
driver.close()