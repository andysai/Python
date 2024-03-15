"""
readline一次读取一行内容
"""

f = open('test.txt','r')
print('第一行:' + f.readline())
print('第二行:' + f.readline())
print('第三行:' + f.readline())
f.close()