"""
reduce(func, lst),其中func必须有2个参数。每次func计算的结果继续和序列的下一个元素做累积计算
"""

# 导入模块
import functools

# 准备列表数据
list1 = [1, 2, 3, 4, 5]

# 定义函数
def func(a, b):
    return a + b

# 验收结果，调用reduce，作用：功能函数计算的结果和序列的下一个数据做累计计算
result = functools.reduce(func, list1)
print(result)