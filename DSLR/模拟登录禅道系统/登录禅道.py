import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://10.12.12.65/zentao/user-login-L3plbnRhby8=.html')
time.sleep(2)
teacher = driver.find_element(By.NAME, 'account').send_keys('935452')
assistant = driver.find_element(By.NAME, 'password').send_keys('dslr#2022')

button = driver.find_element(By.ID, 'submit')
button.click()
time.sleep(2)
driver.close()
