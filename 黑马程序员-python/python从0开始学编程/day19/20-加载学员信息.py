# 2.8 加载学员信息
def load_student(self):
    # 1 打开文件:尝试以r打开，如果有异常w
    try:
        f = open('student.data', 'r')
    except:
        f = open('student.data', 'w')
    else:
        # 2 读取数据:文件读取出的数据是字符串还原列表类型:[{}]转换[学员对象]
        data = f.read()  # 字符串
        new_list = eval(data)
        self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
    finally:
        # 3 关闭文件
        f.close()