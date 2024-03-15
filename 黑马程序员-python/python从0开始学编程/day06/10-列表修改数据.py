name_list = ['Tom','Lily','Rose']
# 1 修改执行下标的数据
name_list[0] = 'aaa'
print(name_list)

# 2 逆序 reverse()
num_list = [1,3,2,5,4,6]
num_list.reverse()
print(num_list)

# 3 sort() 排序:升序 和降序
num_list.sort(reverse=True) # True为升序 False为降序
print(num_list) # 默认升序排序
num_list.sort(reverse=False)
print(num_list)
