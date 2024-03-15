class Furniture():
    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area

    def __str__(self):
        return f'家具名称为{self.name},家具面积为{self.area}'
