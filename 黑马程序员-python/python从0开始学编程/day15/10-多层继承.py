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

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 3 徒弟类，继承师傅类和学校类，添加和父类同名的属性和方法
# 3.1 独创秘方
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake1(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名属性和方法:把父类的同名属性和方法再次封装
    def make_master_cake(self):
        # 初始化父类
        Master.__init__(self)
        # 父类类名.函数()
        Master.make_cake(self)

    def make_school_make(self):
        School.__init__(self)
        School.make_cake(self)

# 4 创建徒孙类，用这个类去撞见对象；用这个对象调用父类的属性或方法看能否成功
class Tusun(Prentice):
    pass

# 4 用徒弟类创建对象，调用实例属性和方法
xiaoqiu = Prentice()
xiaoqiu.make_cake()
xiaoqiu.make_master_cake()
xiaoqiu.make_school_make()