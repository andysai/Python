"""
需求:用户输入学员姓名、性别、手机号，将学员添加到系统
步骤:
    用户输入姓名、性别、手机号
    创建该学员对象
    将该学员对象添加到列表
"""
from student import *
# 2.2 添加学员
def add_student(self):
    # 1 用户输入姓名、性别、手机号
    name = input('请输入您的姓名:')
    gebder = input('请输入您的性别:')
    tel = input('请输入您的手机号:')

    # 2 创建该学员对象 -- 类？类在student文件里面 先导入student模块，再创建对象
    student = Student(name, gebder, tel)

    # 3 将该学员对象添加到列表
    self.student_list.append(student)