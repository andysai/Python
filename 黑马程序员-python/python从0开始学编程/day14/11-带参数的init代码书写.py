# 1 定义类:带参数的init:宽度和高度； 实例方法:调用实例属性
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽为{self.width}')
        print(f'洗衣机的宽为{self.height}')

# 2 创建对象，创建多个对象且属性值不同；调用实例方法
haier1 = Washer(10, 20)
haier1.print_info()

haier2 = Washer(30, 40)
haier2.print_info()