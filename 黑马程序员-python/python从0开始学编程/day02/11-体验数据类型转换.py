"""
1 input

2. 检测input数据类型str

3. int()转换数据类型

4. 检测是否转换成功
"""
number = input('请输入数字:')
print(number)

print(type(number)) # str

print(type(int(number))) # int