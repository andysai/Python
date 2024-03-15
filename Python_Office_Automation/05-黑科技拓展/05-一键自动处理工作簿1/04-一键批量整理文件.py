# 导入模块
import os
import re
import sys

# 用户输入需要更改文件名的路径
path = "../source_material/05/04一键批量整理文件/要整理的文件"

def del_with(fileType, front, back, old):
    os.chdir(path)
    currentpath = os.getcwd()
    fileList = os.listdir(currentpath)

    # 名称变量
    num = 1
    # 遍历文件夹中所有文件
    for fileName in fileList:
        prefix = os.path.splitext(fileName)[0]
        fix = os.path.splitext(fileName)[1]
        # 文件重新命名
        if fix == fileType and os.path.isfile(os.path.join(currentpath, fileName)):
            if (num < 10):
                num_str = '0' + str(num)
            else:
                num_str = str(num)
            if old == False:
                newName = front + num_str + back + fix
            else:
                newName = front + num_str + back + fileName
            os.rename(fileName, newName)
            # 改变编号，继续下一项
            num += 1

    # 刷新
    sys.stdin.flush()
    print("修改后:" + str(os.listdir(currentpath)))

if __name__ == "__main__":
    # 要修改什么类型的文件
    fileTpye = ".png"
    # 前缀
    front = '0'
    # 后缀
    back = '-新图片'
    # 是否保留原文件迷你工资 True False
    old = False
    del_with(fileTpye, front, back, old)
