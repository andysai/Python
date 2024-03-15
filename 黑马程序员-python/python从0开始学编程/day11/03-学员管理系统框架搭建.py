# 定义功能界面函数
def info_print():
    print("-----请选择功能-----")
    print("1 添加学员")
    print("2 删除学员")
    print("3 修改学员信息")
    print("4 查询学员信息")
    print("5 显示所有学员信息")
    print("6 退出系统")
    print("-" * 18)

# 1. 显示功能界面
info_print()

# 系统功能需要循环使用，直到用户输入6，才退出系统
a = True
while a:
    # 2. 用户输入功能序号
    num = int(input("请输入序号(1-6)进行选择："))

    # 3. 按照用户输入的功能序号执行不同的功能(函数)
    # 如果用户输入1，执行添加；如果用户输入2，执行删除... -- 多重判断
    if num == 1:
        print("添加学员")
    elif num == 2:
        print("删除学员")
    elif num == 3:
        print("修改学员信息")
    elif num == 4:
        print("查询学员信息")
    elif num == 5:
        print("显示所有学员信息")
    elif num == 6:
        print("退出系统")
        a = False
    else:
        print("请输入1-6的序号")