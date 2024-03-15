# 方法一
def add_num(a, b):
    return abs(a) + abs(b)

result = add_num(-1, 2)
print(result)

# 方法二
def sum_num(a, b, f):
    return f(a) + f(b)

result = sum_num(-1, 2, abs)
print(result)