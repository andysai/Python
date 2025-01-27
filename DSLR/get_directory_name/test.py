# 导入模块
import os

# path定义需要获取文件名称的目录
path = r'D:\python\DSLR\get_directory_name\a'

# os.listdir()方法获取文件夹名字，返回数组
file_name_list = os.listdir(path)

# 转为字符串
file_name = str(file_name_list)

# replace替换"["、"]"、" "、"'"
file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace(" ", "")

# 创建并打开文件list.txt
f = open(path + "\\" + "文件list.txt", "a")

# 将文件下名称写入到"文件list.txt"
f.write(file_name)