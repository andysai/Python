import xlwings as xw
from tkinter import *
import tkinter.font as tkFont
import os
import time
import datetime

# 写入数据
def input_value(new_file_name):
    app = xw.App(visible=True, add_book=False)

    # 1.打开原工作簿
    workbook = app.books.open(new_file_name)

    # 2.获取所有工作表
    sheet = workbook.sheets[0]
    rows = int(sheet.used_range.address.split("$")[-1])
    for i in range(2, rows + 1):
        time.sleep(0.3)
        D_value = "D" + str(i)
        E_value = "E" + str(i)

        D_value_time = sheet.range(D_value).value
        E_value_time = sheet.range(E_value).value

        d1 = datetime.datetime.strptime(D_value_time, '%H:%M')
        d2 = datetime.datetime.strptime(E_value_time, '%H:%M')

        if len(str(d2 - d1)) < 10:
            sheet.range("F" + str(i)).value = str(d2 - d1)[:-3]
        else:
            sheet.range("F" + str(i)).value = str(d2 - d1)[8:-3]

    time.sleep(10)
    # 3.保存工作簿
    # save_close(app,workbook)

# 2.保存和退出程序
def save_close(app, workbook):
    workbook.save()
    workbook.close()
    app.quit()

# 获取指定后缀的文件
def get_filename(path, filetype):  # 输入路径、文件类型 例如'.csv'
    file_name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if filetype + ' ' in i + ' ':  # 这里后面不加一个字母可能会出问题，加上一个（不一定是空格）可以解决99.99%的情况
                file_name.append(i)
    return file_name  # 输出由有后缀的文件名组成的列表

# python程序执行入口
if __name__ == "__main__":
    path = "../source_material/07/05一键统计加班时长"
    os.chdir(path)
    # 1.先复制原工作簿
    file_name = get_filename(".", ".xlsx")[0]

    # 写入数值
    input_value(file_name)

