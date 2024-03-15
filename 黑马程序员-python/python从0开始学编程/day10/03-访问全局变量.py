# 全局变量指的是在函数体内、外都能生效的变量

# 定义全局变量 a
a = 100

def testA():
    print(a)

def testB():
    print(a)

testA() # 100
testB() # 100
