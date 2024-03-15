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

# 等待存储所有学员的信息
info = []

# 添加学员信息的函数
def add_info():
    """添加学员函数"""
    # 1 用户输入:学号、姓名、手机号
    new_id = input("请输入学号:")
    new_name = input("请输入姓名:")
    new_tel = input("请输入手机号:")

    # 声明info是全局变量
    global info

    # 2 判断是否添加这个学员:如果学员姓名已经存在报错提示，如果姓名不存在添加数据
    for i in info:
        if new_name == i['name']:
            print("该用户已经存在")
            return
    # 如果用户输入的姓名不存在，则添加该学员信息
    info_dict = {}
    # 将用户输入的数据追加到字典
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # print(info_dict)

    # 将这个学员的字典数据追加到列表
    info.append(info_dict)
    print(info)



# 系统功能需要循环使用，直到用户输入6，才退出系统
a = True
while a:
    # 1. 显示功能界面
    info_print()

    # 2. 用户输入功能序号
    num = int(input("请输入序号(1-6)进行选择："))

    # 3. 按照用户输入的功能序号执行不同的功能(函数)
    # 如果用户输入1，执行添加；如果用户输入2，执行删除... -- 多重判断
    if num == 1:
        # print("添加学员")
        add_info()
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
        print("输入的功能序号有误")