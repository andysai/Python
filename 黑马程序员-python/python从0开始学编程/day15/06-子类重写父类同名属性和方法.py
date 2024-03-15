# 1 师傅类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2 学校类，属性和方法
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake1(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 3 徒弟类，继承师傅类和学校类，添加和父类同名的属性和方法
# 3.1 独创秘方
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake1(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 4 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
daqiu.make_cake()

# 结论:如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法