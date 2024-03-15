# 需求1:把aa文件夹所有文件重命名 Python_xxxx
import os

# 1 找到所有文件:获取aa文件夹的目录列表 -- listdir()
file_list = os.listdir('aa')

# 先切换到需要重命名文件的目录
os.chdir('aa')

# 2 构造名字

for i in file_list:
    # new_name = 'Python_' + 原文件i
    new_name = 'Python_' + i

# 3 重命名
    os.rename(i, new_name)