def estimated_number(size,time):
    number = size * 80 / time
    print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (size,time,number))

# 调用工时计算函数
estimated_number(1.5,2)
# 调用人力计算函数
estimated_number(0.8,25)