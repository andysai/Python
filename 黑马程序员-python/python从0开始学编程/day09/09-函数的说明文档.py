# help(len) # help函数作用:查看函数的说明文档(函数的解释说明的信息)

"""
语法:
    def 函数名(参数):
        '''说明文档的位置'''
        :return a + b
help(函数名)
"""


# def sum_num(a,b):
#     """求和函数"""
#     return a + b
#
# help(sum_num)

# 函数的说明文档的高级使用
def sum_num(a,b):
    """
    求和函数sum_num
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a + b

help(sum_num)