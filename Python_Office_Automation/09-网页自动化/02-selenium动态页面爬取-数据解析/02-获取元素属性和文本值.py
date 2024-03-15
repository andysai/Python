# 获取元素属性
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = "https://www.baidu.com/"
# browser.get(url)
# input = browser.find_element_by_id("kw")
# print(input)
# print(input.get_attribute("name"))
# print(input.get_attribute("class"))
# print(input.get_attribute("id"))
# print(input.get_attribute("maxlength"))
# print(input.get_attribute("autocomplete"))
# browser.close()

# 获取元素文本值
# from selenium import webdriver
#
# get_12306 = webdriver.Chrome()
# get_12306.get('https://www.12306.cn/index/index.html')
# a_href = get_12306.find_element_by_link_text('中国铁路12306')
#
# #  获取元素标签的内容
# att01 = a_href.get_attribute('textContent')
# text_01 = a_href.text
#
# # # 获取元素内的全部HTML
# att02 = a_href.get_attribute('innerHTML')
#
# # # 获取包含选中元素的HTML
# att03 = a_href.get_attribute('outerHTML')
#
# # 获取该元素的标签类型
# tag01 = a_href.tag_name
#
# print(att01, '\n' + text_01, '\n' + att02, '\n' + att03, '\n' + tag01)
#
# get_12306.quit()

# 获取ID、位置、标签名
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.baidu.com/'

browser.get(url)

logo = browser.find_element_by_xpath('//div[@id="lg"]/img[@class="index-logo-src"]')
print(logo.id)
print(logo.tag_name)
print(logo.location)
print(logo.size)
browser.close()
browser.quit()


