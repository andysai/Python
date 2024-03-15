# 需求：任意两个数字，先进行数字处理(绝对值或四舍五入)再求和计算
# 方法一
def add_num(a, b):
    return abs(a) + abs(b)

result = add_num(-1, 2)
print(result)

# 方法二：高阶函数：f是第三个参数，用来接收将来传入的函数
def sum_num(a, b, f):
    return f(a) + f(b)

result = sum_num(-1, 2, abs)
print(result)

result = sum_num(1.1, 2.8, round)
print(result)