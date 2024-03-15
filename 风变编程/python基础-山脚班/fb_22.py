# 八、让用户输入一个数字，并指出这个数字是否是10的整数倍
number = int(input("请输入一个数："))
if (number % 10) == 0 :
    print("{}是10的整倍数".format(number))
else:
    print("{}不是10的整倍数".format(number))