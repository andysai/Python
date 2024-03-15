"""
查找:所谓的字符串查找方法即是查找子串在字符串中的位置或出现的次数

    find():检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则返回-1。
    语法:字符串序列.find(子串,开始位置下标,结束位置下标)

    index():检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则报异常。
    语法:符串序列.index(子串,开始位置下标,结束位置下标)

    count():返回某个子串在字符串中出现的次数
    语法:字符串序列.count(子串,开始位置下标,结束位置下标)

    注意:开始和结束位置下标可以省略，表示在整个字符串序列中查找。
"""
mystr = 'hello world and itcast and itheima and Python'

# find()
print(mystr.find('and')) # 出现的第一个字符串的位置 12
print(mystr.find('and')) # 23
print(mystr.find('ands',15,30)) # 返回-1，ands子串不存在

# index()
print(mystr.index('and')) # 出现的第一个字符串的位置 12
print(mystr.index('and')) # 23
# print(mystr.index('ands',15,30)) # 报错，ands子串不存在

# count()
print(mystr.count('and')) # 统计and子串的出现次数 3
print(mystr.count('and',15,30)) # 统计and子串的出现次数 1
print(mystr.count('ands',15,30)) # ands没有出现过，则返回0

# rfind(),rindex(),从右边开始查找，用法和find(),index()一样
