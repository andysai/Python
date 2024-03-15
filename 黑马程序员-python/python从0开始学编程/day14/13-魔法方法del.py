class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __del__(self):
        print(f'{self}对象已经被删除')


haier1 = Washer(10, 20)
# <__main__.Washer object at 0x0000015D1EB0B388>对象已经被删除
del haier1
