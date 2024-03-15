# js滑动页面
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get("http://www.zhihu.com/explore")
# print(browser.page_source)
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# 截屏
from selenium import webdriver

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://blog.csdn.net/Kwoky/article/details/80285201")
# 截屏
driver.save_screenshot("../source_material/02/app2.png")
