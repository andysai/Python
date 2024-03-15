"""
判断:所谓判断即是判断真假，返回的结果是布尔型数据类型:True或False
startswith():检查字符串是否是以指定子串开头，是则返回True,否则返回False。
如果设置开始和结束位置下标，则在指定范围内检查。
语法:字符串序列.startswith(子串,开始位置下标,结束位置下标)

endswith():检查字符串是否是以指定子串结尾，是则返回True,否则返回False。
如果设置开始和结束位置下标，则在指定范围内检查。
语法:字符串序列.startswith(子串,开始位置下标,结束位置下标)
"""
mystr = 'hello world and itcast and itheima and Python'

# 结果:True
print(mystr.startswith('hello'))

# 结果:False
print(mystr.startswith('helw'))

# 结果:True
print(mystr.endswith('Python'))

# 结果:False
print(mystr.endswith('python'))