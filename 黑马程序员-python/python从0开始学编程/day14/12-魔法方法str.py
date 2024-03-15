class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return '这是海尔洗衣机的说明书'

haier1 = Washer(10, 20)
# 这是海尔洗衣机的说明书
print(haier1)
