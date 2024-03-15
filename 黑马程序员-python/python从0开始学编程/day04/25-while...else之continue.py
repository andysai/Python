# 因为continue是退出当前一次循环，继续下一次循环，所以该循环在continue控制下是可以正常结束的，当循环结束后，则执行了else缩进的代码
i = 1
while i <= 5 :
    if i == 3 :
        i += 1
        print('只2遍不真诚，继续')
        continue
    print('媳妇儿，我错了')
    i += 1
else:
    print('媳妇儿原谅我了...')