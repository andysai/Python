class Washer():
    def wash(self):
        print('洗衣服')

haier1 = Washer()

# 添加属性:对象名.属性名 = 值
haier1.width = 500
haier1.height = 800

# 获取属性 对象名.属性名
print(f'haier1洗衣机的宽度是{haier1.width}')
print(f'haier1洗衣机的高度是{haier1.height}')