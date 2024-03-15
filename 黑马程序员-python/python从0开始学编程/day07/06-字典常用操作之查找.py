# 注意：如果当前查找的key存在，则返回对应的值；否则则报错
dict1 = {'name':'Tom','age':20,'gender':'男'}

# 1 [key]
#print(dict1['name'])
# print(dict1['id'])

# 2 函数
# get()
# 字典序列.get(key,默认值)
# 注意：如果当前查找的key不存在则返回第二个参数(默认值),如果省略第二个参数，则返回None
print(dict1.get('name'))
print(dict1.get('id',110))
print(dict1.get('id'))

# keys() 查找字典中所有的key，返回可迭代对象
print(dict1.keys())

# values() 查找字典中所有的value，返回可迭代对象
print(dict1.values())

#items() 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是字典的key，元组数据2是字典key对应的值
print(dict1.items())