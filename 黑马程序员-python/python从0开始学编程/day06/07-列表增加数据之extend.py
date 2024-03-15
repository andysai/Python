name_list = ['Tom','Lily','Rose']

# extend:列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
name_list.extend('xiaoming')
print(name_list)

name_list.extend(['aa','bb'])
print(name_list)