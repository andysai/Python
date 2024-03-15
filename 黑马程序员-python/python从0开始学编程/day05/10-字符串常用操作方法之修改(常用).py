"""
修改:
    replace():替换
    语法:字符串序列.replace(旧子串,新子串,替换次数)

    split():按照指定字符分割字符串
    语法: 字符串序列.split(分割字符,num)
    注意: num表示的是分割字符出现的次数，即将来返回数据个数为num+1个

    join():用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串
    语法:字符串序列.join(多字符串组成的序列)

"""
mystr = 'hello world and itcast and itheima and Python'

# 结果: hello world he itcast he itheima he Python
print(mystr.replace('and','he'))

# 结果:hello world he itcast he itheima he Python
print(mystr.replace('and','he',10))

# 结果:['hello world ', ' itcast ', ' itheima ', ' Python']
print(mystr.split('and')) # 分隔符会丢失

# 结果:
mylist = ['aa','bb','cc']
# aa...bb...cc...
print('...'.join(mylist))
