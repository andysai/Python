"""
创建集合
集合数据的特点
集合的常见操作
"""

# 创建集合使用{}或set()，但是如果要创建空集合只能使用set()，因为{}用来创建空字典
s1 = {10,20,30,40,50}
print(s1)

s2 = {10,30,20,10,30,40,30,50}
print(s2)

s3 = set('abcdefg')
print(s3)

s4 = set()
print(type(s4)) # set

s5 = {}
print(type(s5)) #dict