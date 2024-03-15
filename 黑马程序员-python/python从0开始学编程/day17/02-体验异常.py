"""
语法:
    try:
        可能发生错误的代码
    except:
        如果出现异常执行的代码
"""

try:
    a = open('a.txt', 'r')
except:
    a = open('a.txt', 'w')

