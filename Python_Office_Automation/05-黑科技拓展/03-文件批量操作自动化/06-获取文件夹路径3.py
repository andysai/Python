# 导入模块
import os, shutil
import sys

# 获取文件夹文件的操作
def arrange_file(dir_path0):
    for dirpath, dirnames, filenames in os.walk(dir_path0):
        # print(dirpath) # 获取所有的文件夹路径(不含文件),返回路径字符串
        # print(dirnames) # 获取文件夹下的所有文件夹名字，返回文件夹名字的列表
        print(filenames) # 获取所有的文件名(不包含文件夹),返回问及爱你名字的列表

arrange_file("../source_material/03/01一键批量整理文件")