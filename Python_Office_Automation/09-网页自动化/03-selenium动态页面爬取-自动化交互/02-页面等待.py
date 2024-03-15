"""
标题是某内容:title is
标题包含某内容:title_contains
元素加载出，传入定位元组，如(by.ID, 'p'):presence_of_element_located
元素可见，传入定位元组:visibility_of_element_located
可见，传入元素对象:visibility_of
所有元素加载出:presence_of_all_elements_located
某个元素文本包含某文字:text_to_be_present_in_element
某个元素值包含某文字:text_to_be_present_in_element_value
加载并切换:frame_to_be_available_and_switch_to_it_frame
元素不可见:invisibility_of_element_located
元素可点击:element_to_be_clickable
判断一个元素是否仍在DOM，可判断页面是否已经刷新:staleness_of
元素可选择，传元素对象:element_to_be_selected
元素可选择，传入定位元组:element_located_to_be_selected
传入元素对象以及状态，相等返回True，否则返回False:element_selection_state_to_be
传入定位元组以及状态，相等返回True，否则返回False:element_located_selection_state_to_be
是否出现Alert:alert_is_present
"""

# 显式等待
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # WebDriverWait 库，负责循环等待
# from selenium.webdriver.support.ui import WebDriverWait
# # expected_conditions 类，负责条件触发
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# # 生成智能等待的对象
# wait = WebDriverWait(driver, 10) # 最长等待的时间，单位是秒
# try:
#     # 页面一直循环，直到 id="myDynamicElement" 出现
#     element = wait.until(
#         EC.presence_of_element_located((By.ID, "suvv"))
#     )
#     print(element)
# except Exception as e:
#     print('error.', e)
# finally:
#     driver.quit()

# 隐式等待
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.implicitly_wait(10) # seconds
myDynamicElement = driver.find_element_by_id("su")
print(myDynamicElement)
driver.quit()
