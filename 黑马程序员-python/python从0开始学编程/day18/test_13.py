# 定义多个功能，把某个功能添加到__all__
# __all__ = ['testA']
__all__ = ['testA', 'testB'] # 调用多个的写法

def testA():
    print('testA')

def testB():
    print('testB')