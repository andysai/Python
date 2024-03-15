# 导入模块
import os
import re
import sys

def del_with():
    path = "../source_material/04/01一键批量整理文件"
    os.chdir(path)
    currentpath = os.getcwd()
    fileList = os.listdir(currentpath)
    print(currentpath)
    # 名称变量
    num = 1
    # 遍历文件夹中所有文件
    for fileName in fileList:
        prefix = os.path.splitext(fileName)[0]
        fix = os.path.splitext(fileName)[1]
        print(fileName)
        print(fix)
        num += 1
        print(os.path.isfile(os.path.join(currentpath, fileName)))
del_with()