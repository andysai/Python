print("猜大小游戏")
while True:
    my_number = 24
    your_number = int(input("猜一猜我想的数字是多少:"))
    if my_number == your_number:
        print("猜对了")
        break
    elif my_number > your_number:
        print("太小了")
    else:
        print("太大了")