# 定义全局变量 a
a = 100

def testA():
    print(a)

def testB():
    global a # 修改全局变量 声明a为全局变量
    a = 200 # 如果直接修改a=200,此时的a是全局a还是局部a
    # 因为在全局位置(B函数调用后)打印a得到的不是200而是100
    print(a)

testA() # 100
testB() # 200
print(f'全局变量a = {a}')

"""
总结:
    1.如果在函数里面直接把变量a=200赋值，此时的a不是全局变量的修改，而是相当于在函数内部声明了一个新的局部变量
    2.函数体内部修改全局变量:先global声明a为全局变量，然后再变量重新赋值
"""