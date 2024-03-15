class StudentManager(object):
    def __init__(self):
        # 存储学员数据 -- 列表
        self.student_list = []

    # 一 程序入口函数
    def run(self):
        # 1 加载文件里面的学员数据

        while True:
            # 2 显示功能菜单
            # 3 用户输入目标功能序号
            menu_num = int(input('请输入您需要的功能序号(1-7):'))

            # 4 根据用户输入的序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                pass
            elif menu_num == 2:
                # 删除学员
                pass
            elif menu_num == 3:
                # 修改学员信息
                pass
            elif menu_num == 4:
                # 查询学员信息
                pass
            elif menu_num == 5:
                # 显示所有学员信息
                pass
            elif menu_num == 6:
                # 保存学员信息
                pass
            elif menu_num == 7:
                # 退出系统 -- 退出循环
                break
            else:
                print('请输入1-7的序号进行选择')

    # 二 系统功能函数