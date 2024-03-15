import math

# 方法1，关键词：条件判断
def abs_value1():
    number = float(input("请输入一个数值:"))
    if number >= 0 :
        number = number
    else:
        number = -number
    print('绝对值为：%d' % int(number))

# 方法2，关键词：内置函数
def abs_value2():
    number = float(input('2.请输入一个数字：'))
    number = abs(number)
    print('绝对值为：%d' % int(number))

# 方法3，关键词：内置模块
def abs_value3():
    number = float(input('3.请输入一个数字：'))
    number = math.fabs(number)
    print('绝对值为：%d' % int(number))

# 写完3种方法后，验证一下吧。
abs_value1()
abs_value2()
abs_value3()
