import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 创建一个 Edge 实例
driver = webdriver.Edge()
# driver = webdriver.Firefox()

# 打开一个网页
driver.get("https://www.morningstar.cn/fundselect/default.aspx")
driver.implicitly_wait(200)

# 通过配置按钮选择对应选项
# 选择基金组别
button_jjzb = driver.find_element(By.ID, "ctl00_cphMain_cblGroup_0")
button_jjzb.click()

# 选择三年评级
button_Rating3 = driver.find_element(By.ID, "ctl00_cphMain_cblStarRating_0")
button_Rating3.click()

# 选择五年评级
button_Rating5 = driver.find_element(By.ID, "ctl00_cphMain_cblStarRating5_0")
button_Rating5.click()

# 选择业绩总回报
# 三个月
button_rbM31 = driver.find_element(By.ID, "ctl00_cphMain_ucPerformance_rbM31")
button_rbM31.click()

# 六个月
button_rbM61 = driver.find_element(By.ID, "ctl00_cphMain_ucPerformance_rbM61")
button_rbM61.click()

# 一年
button_rbY11 = driver.find_element(By.ID, "ctl00_cphMain_ucPerformance_rbY11")
button_rbY11.click()

# 两年(年化)
button_rbY21 = driver.find_element(By.ID, "ctl00_cphMain_ucPerformance_rbY21")
button_rbY21.click()

# 三年(年化)
button_rbY31 = driver.find_element(By.ID, "ctl00_cphMain_ucPerformance_rbY31")
button_rbY31.click()

# 五年(年化)
button_rbY51 = driver.find_element(By.ID, "ctl00_cphMain_ucPerformance_rbY51")
button_rbY51.click()

# 基金分类
button_gory = driver.find_element(By.ID, "ctl00_cphMain_cblCategory_16")
button_gory.click()

# 资产净值
button_zcjz = driver.find_element(By.ID, "fs_slider_tna")
# button_zcjz = driver.find_element(By.CSS_SELECTOR, "ui-slider-handle ui-state-default ui-corner-all")
# action = ActionChains(driver)
# action.click_and_hold(button_zcjz)
# action.move_by_offset(0, 0)

# action.release().perform()
# action.click_and_hold(button_zcjz).move_by_offset(0, 40).release().perform()

# button_zcjz.click()
button_zcjz1 = button_zcjz.find_element(By.CLASS_NAME, "ui-slider-handle ui-state-default ui-corner-all ui-state-hover ui-state-active ui-state-focus").find_element(By.XPATH, "//input[@value='left: 40%;']")

button_zcjz1.click()

# 查询
# button_check = driver.find_element(By.ID, "ctl00_cphMain_btnGo")
# button_check.click()

#
# 打印页面标题

print(button_zcjz)
time.sleep(2)
# 关闭浏览器
driver.quit()



