class Furniture():
    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area

    def __str__(self):
        return f'家具名称为{self.name},家具面积为{self.area}'


class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.frunitrue = []


    def __str__(self):
        return f'房屋地理位置在{self.address}, 房屋面积是{self.area}, 剩余面积{self.free_area}, 家具有{self.frunitrue}'


# 双人床，6
bad = Furniture('双人床', 6)
print(bad)
sofa = Furniture('沙发', 10)
print(sofa)

# 房子1: 北京， 1000
jia1 = Home('北京', 1000)
print(jia1)