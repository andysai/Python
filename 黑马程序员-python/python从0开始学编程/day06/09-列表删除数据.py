name_list = ['Tom','Lily','Rose']
# 1 del
# del name_list
# del(name_list)
# del可以删除指定下标的数据
# del name_list[0]
# print(name_list)

# 2 pop():删除指定下标的数据,默认为最后一个，并返回该数据
# del_name = name_list.pop()
# del_name = name_list.pop(1)
# print(del_name)
# 3print(name_list)

# 3 remove():移除列表中某个数据的第一个匹配项
# name_list.remove('Rose')
# print(name_list)

# 4 clear():清空列表
name_list.clear()
print(name_list)