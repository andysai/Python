# 1.定义两个函数
# 2.函数一有返回值50；函数二把返回值50作为参数传入(定义函数二要有形参)

def test1():
    return 50

def test2(num):
    return num

result = test1()

print(test2(result))