# 2.7 保存学员信息
def save_student(self):
    # 1 打开文件
    f = open('student.data', 'w')

    # 2 文件写入数据
    # 2.1 [学员对象]转换成[字典]
    new_list = [i.__dict__ for i in self.student_list]

    # 2.2 文件写入 字符串数据
    f.write(str(new_list))

    # 3 关闭文件
    f.close()
