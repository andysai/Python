"""
index():返回指定数据所在位置的额下标
语法:
    列表序列.index(数据,开始位置下标,结束位置下标)
"""
name_list = ['Tom','Lily','Rose']
print(name_list.index('Lily',0,2)) # 1

# count():统计指定数据在当前列表中出现的次数
print(name_list.count('Lily')) # 1

# len():访问列表长度，即列表中数据的个数
print(len(name_list)) # 3