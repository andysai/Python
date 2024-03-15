# 你好$$$我正在学 Python@#@#现在需要&*&*修改字符串
import re

a = '你好$$$我正在学 Python@#@#现在需要&*&*修改字符串'
b = a.replace("$$$", " ").replace("@#@#", " ").replace("&*&*", " ")
print(b)


