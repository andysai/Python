t1 = ('aa','bb','cc','dd')
# 元组数据不支持修改，只支持查找
# 1 按下标查找数据
print(t1[1])

# 2 index():查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index方法相同
print(t1.index('aa'))

# 3 count():统计某个数据在当前元组出现的次数
print(t1.count('bb'))

# 4 len():统计元组中数据的个数
print(len(t1))