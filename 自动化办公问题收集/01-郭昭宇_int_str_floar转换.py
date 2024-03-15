"""
字符串直接转换为int类型的话，里面不能是浮点型或者带英文之类的只能是数字;
如果是小数需转换成int类型的话，需先转换成float再转为int，否者会报错;
如果是带英文字母或者特殊字符的，是无法转换为int或者float
"""

b = input("请输入:")
b = int(b)

print(b)
# print(type(b))
# print(a)
# print(type(a))