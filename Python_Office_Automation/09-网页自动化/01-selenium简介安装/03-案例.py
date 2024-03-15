# 导入 webdriver
from selenium import webdriver
import time

# 调用环境变量指定的Chrome浏览器创建浏览器对象
driver = webdriver.Chrome()
print(type(driver))

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择time.sleep()
driver.get('https://www.baidu.com/')
time.sleep(2)

# 打印渲染后的源代码
print(driver.page_source)

# 打印页面标题“百度一下，你就知道”
print(driver.title)

# 获取当前url
print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()

# 关闭浏览器
driver.quit()
