"""
需求:用户输入目标学员姓名，如果学员存在则删除该学员
步骤:
    用户输入目标学员姓名
    遍历学员数据列表，如果用户输入的学员姓名存在则删除，否则则提示该学员不存在
"""


# 2.3 删除学员
def del_student(self):
    # 1 用户输入目标学员姓名
    del_name = input('请输入需要删除的学员姓名:')

    # 2 遍历学员数据列表，如果用户输入的学员姓名存在则删除，否则则提示该学员不存在
    for i in self.student_list:
        if del_name == i.name:
            # 删除该学员对象
            self.student_list.remove(i)
            break
    else:
        # 循环正常结束执行的代码，循环结束都没有删除任何一个对象，所以说明用户输入的目标学员不存在
        print('查无此人')

    # 测试
    # print(self.student_list)