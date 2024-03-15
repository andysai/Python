import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(2)
button = driver.find_element_by_class_name('comment__show_all')
button.click()
time.sleep(2)
res = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')
for i in res:
    a = i.find_element_by_tag_name('p')
    print(a.text)
driver.close()