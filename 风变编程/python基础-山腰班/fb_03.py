# 把之前这段for循环的代码改成while循环，要求运行效果相同
a=0
while a < 5:
    b = int(input('请输入0结束循环，你有5次机会:'))
    a += 1
    if b == 0:
        print('你触发了break语句，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')