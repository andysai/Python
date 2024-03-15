print("猜大小游戏")
i = 3
my_number = int(input("心里随便想一个数:"))
while i > 0 :
    your_number = int(input("猜一猜我想的数字是多少:"))
    if my_number == your_number:
        print("猜对了")
        break
    elif my_number > your_number:
        print("太小了")
    else:
        print("太大了")
    i -= 1
    print("你还有%d次机会" % i)
else:
    print("3次都猜不中,失败了")