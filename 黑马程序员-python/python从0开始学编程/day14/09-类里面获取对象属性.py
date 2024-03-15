# 定义类
class Washer():
    def print_info(self):
        # 类里面获取实例属性
        print(f'haier1洗衣机的宽度是{haier1.width}')
        print(f'haier1洗衣机的高度是{haier1.height}')

# 创建对象
haier1 = Washer()

# 添加实例属性
haier1.width = 500
haier1.height = 800


haier1.print_info()