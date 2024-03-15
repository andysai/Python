"""
需求:用户输入目标学员姓名，如果学员存在则修改该学员信息
步骤:
    用户输入目标学员姓名
    遍历学员数据列表，如果用户输入的学员姓名存在则修改学员的姓名、性别、手机号数据，否则则提示该学员不存在
"""
# 2.4 修改学员信息
def modify_student(self):
    # 1 用户输入目标学员姓名
    modify_name = input('请输入需要修改的学员姓名:')
    # 2 遍历数据列表，如果学员姓名存在则修改学员的姓名、性别、手机号数据，否则则提示该学员不存在
    for i in self.student_list:
        if modify_name == i.name:
            i.name = input('姓名:')
            i.gebder = input('性别:')
            i.tel = input('手机号:')
            print(f'修改学员信息成功，姓名{i.name}, 性别{i.gebder}, 手机号{i.tel}')
            break
    else:
        print('查无此人')