"""
打开文件
读写等操作
关闭文件
"""

f = open('test.txt','w')
f.write('sai')
f.close()

a = open('test.txt','r')
print(a.read())
a.close()