# 1.今年我的年龄是x岁
age = 18
print('今年我的年龄是%s岁' % age)

# 2.我的名字是x
name = 'sai'
print('我的名字是%s' % name)

# 3.我的体重是x公斤
weight = 75.5
print('我的体重是%.1f' % weight + '公斤')

# 4.我的学号是x
stu_id = 23
print('我的学号是%d' % stu_id)

# 4.1我的学号是001 %03d不足补全输出，足够的直接输出
stu_id = 1
stu_id2 = 1000
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)

# 5.我的名字是x，今年x岁了
print('我的名字是%s，今年%d岁了' % (name,age))
# 6.我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重%.1f公斤，学号是%d' % (name,age,weight,stu_id))

