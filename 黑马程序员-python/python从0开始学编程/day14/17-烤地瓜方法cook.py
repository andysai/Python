# 1 定义类:初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 烤的状态
        self.state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        # 1 计算地瓜整体烤过的时间
        self.cook_time += time
        # 2 用整体烤过的时间再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            self.state = '生的'

        elif 3 <= self.cook_time < 5:
            self.state = '半生不熟'

        elif 5 <= self.cook_time < 8:
            self.state = '熟的'

        elif self.cook_time >= 8:
            self.state = '烤糊了'

        print(self.state)

# 2 创建对象并调用对应的实例方法
food = SweetPotato()
food.cook(2)
food.cook(2)
food.cook(2)