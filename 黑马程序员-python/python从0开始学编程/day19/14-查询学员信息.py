"""
需求:用户输入目标学员姓名，如果学员存在则打印该学员信息
步骤:
    用户输入目标学员姓名
    遍历学员数据列表，如果用户输入的学员姓名存在则打印学员信息，否则提示该学员不存在
"""

# 2.5 查询学员信息
def search_student(self):
    # 1 用户输入目标学员姓名
    search_name = input('请输入需要查询的学员信息:')

    # 2 遍历学员数据列表，如果用户输入的学员姓名存在则打印学员信息，否则提示该学员不存在
    for i in self.student_list:
        if search_name == i.name:
            print(f'姓名{i.name}, 性别{i.gebder}, 手机号{i.tel}')
            break
    else:
        print('查无此人')