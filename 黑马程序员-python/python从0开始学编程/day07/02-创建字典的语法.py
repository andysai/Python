"""
字典的特点
    符号为大括号
    数据为键值对形式出现
    各个键值对之间用逗号隔开
"""

# 有数据字典：name的值Tom，age的值是20，gender的值是男
dict1 = {'name':'Tom','age':20,'gender':'男'}

print(dict1)
# 空字典
dict2 = {}
dict3 = dict()

print(dict2)
print(type(dict2))
print(dict3)
print(type(dict3))

# 注意：一般称冒号前面的为键(key)，简称k；冒号后面的为值(value),简称v