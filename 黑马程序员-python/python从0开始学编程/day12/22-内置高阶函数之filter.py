"""
filter(func, lst)函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。如果要转换为列表，可以使用list()来转换
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 定义功能函数：过滤序列中的偶数
def func(x):
    return  x % 2 == 0

# 调用filter
result = filter(func, list1)
print(result)
print(list(result))