import time
from selenium import webdriver

driver = webdriver.Chrome()
# 注册账号
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php?action=register')
time.sleep(2)
user_login = driver.find_element_by_id('user_login')
user_login.send_keys('sai')
user_email = driver.find_element_by_id('user_email')
user_email.send_keys('344319484@qq.com')
button = driver.find_element_by_id('wp-submit')
button.click()
driver.close()
