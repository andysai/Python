"""
注意:
    1 __init__()方法，在创建一个对象时默认被调用，不需要手动调用
    2 __init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去
"""

# 目标:定义init魔法方法设置初始化属性，并访问调用
"""
1 定义类
    init魔法方法:width和height
    添加实例方法:访问实例属性
2 创建对象
3 验证成果
    调用实例方法
"""

class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣机的宽为{self.width}')
        print(f'洗衣机的宽为{self.height}')

haier = Washer()
haier.print_info()