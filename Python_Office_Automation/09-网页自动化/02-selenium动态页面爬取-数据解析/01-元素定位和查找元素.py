"""
定位元素
    selenium提供了8种定位方式
        1 id
        2 name
        3 class name
        4 tag name
        5 link text
        6 xpath
        7 css selector
        8 partial link text
"""
from selenium import webdriver

# 单个元素查找
# browser = webdriver.Chrome()

# browser.get("https://www.taobao.com/")
# input_one = browser.find_element_by_id("q")
# input_two = browser.find_element_by_css_selector("#q")
# input_three = browser.find_elements_by_xpath("//*[@id='q']")
# # 渲染后的源码
# print(browser.page_source)
# print(input_one)
# print(input_two)
# print(input_three)
# browser.close()
# browser.quit()

# 多个元素查找
from selenium import webdriver

# 获取商品分类
browser = webdriver.Chrome()
browser.get("https://www.taobao.com/")
css = browser.find_elements_by_css_selector(".service-bd li")
print(len(css))
tag = browser.find_elements_by_tag_name('li')
print(len(tag))
cla_name = browser.find_elements_by_class_name("service-bd")
print(len(cla_name))
xpth = browser.find_elements_by_xpath("//div[@class='service J_Service']")
print(len(xpth))
link_text = browser.find_elements_by_link_text('美妆')
print(len(link_text))
browser.close()
