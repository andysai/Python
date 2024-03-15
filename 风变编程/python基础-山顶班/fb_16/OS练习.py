import os
path = r'D:\python\风变编程\python基础-山顶班\fb_16'
path1 = 'test_01'
path2 = 'fb_csv-01-获取网页内容.py'
print(os.getcwd())  # 返回当前工作目录
print(os.listdir(path))   # 返回path指定的文件夹包含的文件或文件夹的名字的列表
#print(os.mkdir(path1))  # 创建文件夹
print(os.path.abspath(path))   # 返回绝对路径
print(os.path.basename(path))   # 返回文件名
print(os.path.isfile(path2))   # 判断路径是否为文件
print(os.path.isdir(path1))   # 判断路径是否为目录