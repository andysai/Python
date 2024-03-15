"""
需求:打印所有学员信息
步骤:
    遍历学员数据列表，打印所有学员信息
"""

# 2.6 显示所有学员信息
def show_student(self):
    print('姓名\t性别\t手机号')
    # 1 遍历学员数据列表，打印所有学员信息
    for i in self.student_list:
        print(f'{i.name}\t{i.gebder}\t{i.tel}')