class Student(object):
    def __init__(self, name, gender, tel):
        # 姓名、性别、手机号
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'姓名:{self.name},性别:{self.gender},手机号:{self.tel}'

# if __name__ == '__main__':
#     aa = Student('aa', '女', '11')
#     print(aa)