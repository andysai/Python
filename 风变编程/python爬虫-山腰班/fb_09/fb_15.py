import time
from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('吴枫')
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('酱酱')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(2)
page_source = driver.page_source
suops = BeautifulSoup(page_source,'html.parser').find('div',class_='content')
name = suops.find('h1')
message = suops.find('p')

print(name.text + "\n" + message.text.replace(' ',''))
driver.close()