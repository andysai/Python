import time
from selenium import webdriver

# 发布评论
driver = webdriver.Chrome()
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)
user_login = driver.find_element_by_id('user_login')
user_login.send_keys('spiderman')
user_email = driver.find_element_by_id('user_pass')
user_email.send_keys('crawler334566')
button = driver.find_element_by_id('wp-submit')
button.click()
time.sleep(2)
class_name = driver.find_element_by_link_text('未来已来（三）——同九义何汝秀')
class_name.click()
time.sleep(2)
message = driver.find_element_by_id('comment')
message.send_keys('人哪有好的，只是坏的程度不一样而已。(测试selenium测试)')
button1 = driver.find_element_by_id('submit')
button1.click()
driver.close()