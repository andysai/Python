str1 = 'itheima'

# break
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
else:
    print('循环正常结束执行的else代码')

# continue
for i in str1:
    if i == 'e':
        print('遇到e跳过')
        continue
    print(i)
else:
    print('循环正常结束执行的else代码')