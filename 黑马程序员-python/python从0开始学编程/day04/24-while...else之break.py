# 所谓的else指的是循环正常结束之后要执行的代码，即如果break终止循环的情况，else下方缩进的代码将不执行
i = 1
while i <= 5 :
    if i == 3 :
        print('这遍说的不真诚')
        break
    print('媳妇儿，我错了')
    i += 1
else:
    print('媳妇儿原谅我了...')