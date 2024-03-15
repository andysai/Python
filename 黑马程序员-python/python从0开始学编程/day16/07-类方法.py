"""
类方法
    类方法特点
        需要用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须时类对象，一般以cls作为第一个参数
"""
# 1 定义类:私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    # 定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth


class Dog1(object):
    __tooth = 10

    def get_tooth1(self):
        return self.__tooth
# 2 创建对象，调用类方法
wangcai = Dog()
result = wangcai.get_tooth()
print(result)

xiaohei = Dog1()
result1 = xiaohei.get_tooth1()
print(result1)