"""
map(func,lst)，将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(python2)/迭代器(python3)返回
"""

# 准备列表数据
list1 = [1, 2, 3, 4, 5]

# 准备二次方计算的函数
def func(x):
    return x ** 2

# 调用map
result = map(func, list1)

# 验收成果
print(result) # <map object at 0x000001FD08F2B708> 内存地址
print(list(result)) # [1, 4, 9, 16, 25]