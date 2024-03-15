# 七、创建一个字典，在其中存储三个国家中国，非洲，俄罗斯和相对应的肤色：黄色，黑色，白色
dict = {'中国':'黄色','非洲':'黑色','俄罗斯':'白色'}

# 7.1 使用循环将该字典中每个国家的名字打印出来
for key in dict.keys():
    print(key)
# 7.2 使用循环将字典中每个国家对应的肤色打印出来
for value in dict.values():
    print(value)

# 7.3 使用item()函数将字典的中每个国家和相对应的肤色一起打印出来
for key,value in dict.items():
    print(key,value)
