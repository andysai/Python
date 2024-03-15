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
    print(f"{new_name}的学员信息添加成功")

# 删除学员信息
def del_info():
    # 1 用户输入需要删除的学员信息
    del_name = input("请输入需要删除的学员姓名:")
    # 2 检查这个学员是否存在
    global info

    for i in info:
        # 2.1 如果学员存在，则执行删除
        if del_name == i['name']:
            info.remove(i)
            print(f"{del_name}的学员信息删除成功")
            break
    # 2.2 如果学员不存在，则提示“该学员不存在”
    else:
        print("该学员不存在")

# 修改学员信息
def modify_info():
    # 1 用户输入目标学员姓名
    modify_name = input("请输入需要修改学员信息的学员姓名:")
    # 2 检查这个学员是否存在，存在修改手机号，不存在，提示
    # 2.1 声明info是全局变量
    global info
    # 2.2 遍历info
    for i in info:
        # 2.3 如果存在，则修改这位学员的信息，例如手机号
        if modify_name == i['name']:
            i['tel'] = input("请输入需要修改的手机号:")
            print(f"{modify_name}的学员信息修改成功")
            break
    # 2.4 如果不存在，则报错
    else:
        print("该学员不存在")

# 查询学员信息
def search_info():
    # 1 用户输入需要查找的学员姓名
    search_name = input("请输入需要查询的学员姓名:")
    # 2 检查这个学员是否存在，存在执行打印信息，不存在，提示
    # 2.1 声明info是全局变量
    global info
    # 2.2 遍历info
    for i in info:
        # 2.3 学员如果存在，则打印信息
        if search_name == i['name']:
            print("------查询到的学员信息如下------")
            print(f"学号为{i['id']}\n姓名为{i['name']}\n手机号为{i['tel']}")
            print("-" * 29)
            print("\n")
            break
    # 2.4 学员不过不存在，则报错提示
    else:
        print("该学员不存在")

# 显示所有学员信息
def print_all():
    """显示所有学员信息"""
    for i in info:
        print(f"学号:{i['id']}\t姓名:{i['name']}\t手机号:{i['tel']}")

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
        # print("删除学员")
        del_info()
    elif num == 3:
        # print("修改学员信息")
        modify_info()
    elif num == 4:
        # print("查询学员信息")
        search_info()
    elif num == 5:
        # print("显示所有学员信息")
        print_all()
    elif num == 6:
        print("退出系统")
        a = False
    else:
        print("输入的功能序号有误")