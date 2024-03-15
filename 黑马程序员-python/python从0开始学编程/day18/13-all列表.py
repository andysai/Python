"""
__all__
    如果一个模块文件中有__all__变量，当使用from xxx import *导入时，只能导入这个列表中的元素
"""

from test_13 import *
testA()
# 因为test函数没有添加到all列表，只有all列表里面的功能才能导入
testB()