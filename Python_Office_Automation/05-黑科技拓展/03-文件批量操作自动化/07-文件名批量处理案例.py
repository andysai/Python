# 导入模块
import os
import re
import time

# 获取指定后缀的文件，比如获取文件第07章:xulie-字典中所有的.mp4文件
def get_filename(path, filetype): # 输入路径、文件类型 例如:.csv
    file_name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if filetype+"" in i+"":
                file_name.append(i)
    return file_name # 输出由有后缀的文件名组成的列表

if __name__ == "__main__":
    namefile = "../source_material/03/01一键批量整理文件/"
    namelist = get_filename(namefile, ".txt")
    for file_name in namelist:
        used_name = namefile + "/" + file_name
        new_name = used_name[:-4] + ".mp4"
        os.rename(used_name, new_name)
    print("文件命名成功")
