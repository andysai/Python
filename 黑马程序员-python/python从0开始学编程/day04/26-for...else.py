"""
语法:
    for 临时变量 in 序列:
        重复执行的代码
        ...
    else:
        循环正常结束之后要执行的代码
"""
# 所谓的else指的是循环正常结束之后要执行的代码，即如果是break终止循环的情况，else下方缩进的代码将不执行
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束执行的else代码')