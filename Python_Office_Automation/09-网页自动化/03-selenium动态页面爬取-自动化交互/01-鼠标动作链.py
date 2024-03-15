"""
单击鼠标左键:click(on_element=None)
点击鼠标左键，不松开:click_and_hold(on_element=None)
点击鼠标右键:context_click(on_element=None)
双击鼠标左键:double_click(on_element=None)
拖拽到某个元素然后松开:drag_and_drop(source, target)
拖拽到某个坐标然后松开:drag_and_drop_by_offset(source, xoffset, yoffset)
按下某个键盘上的键: key_down(value, element=None)
松开某个键: key_up(value, element=None)
鼠标从当前位置移动到某个坐标:move_by_offset(xoffset, yoffset)
鼠标移动到某个元素:move_to_element(to_element)
移动到距某个元素(左上角)多少距离的位置:move_to_element_with_offset(to_element, xoffset, yoffset)
执行链中的所有动作:perform()
在某个元素位置松开鼠标左键:release(on_element=None)
发送某个键到当前焦点的元素:send_keys(*keys_to_send)
发送某个键到指定元素:send_keys_to_element(element, *keys_to_send)
"""

# 模拟点击
# 导入 webdriver
from selenium import webdriver
import time
# 调用环境变量指定的 Chrome 浏览器创建浏览器对象
driver = webdriver. Chrome ()
# get 方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择
time.sleep(2)
driver.get("http://www.baidu.com/")
# id=“kw”是百度搜索输入框，输入字符串“python”
driver.find_element_by_id('kw').send_keys('python')
# id="su"是百度搜索按钮， click() 是模拟点击
driver.find_element_by_id("su").click()
# 获取新的页面快照
driver.save_screenshot("python1.png")
# 清除输入框内容
driver.find_element_by_id("kw").clear()
print('访问成功')
