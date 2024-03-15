i = 2
sum = 0
while i < 101:
    sum = sum + i
    i += 2 # 如果不加计数器，循环会卡死，进行到死循环状态
print(sum)