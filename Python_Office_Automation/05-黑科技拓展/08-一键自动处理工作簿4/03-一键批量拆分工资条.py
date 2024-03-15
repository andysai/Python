import xlwings as xw
import time
from datetime import datetime
import os
import random
from tkinter import *
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中
import tkinter.font as tkFont

# 获取指定后缀的文件
def get_filename(path, filetype):  # 输入路径、文件类型 例如'.csv'
    file_name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if filetype + ' ' in i + ' ':  # 这里后面不加一个字母可能会出问题，加上一个（不一定是空格）可以解决99.99%的情况
                file_name.append(i)
    return file_name  # 输出由有后缀的文件名组成的列表

# 2.保存和退出程序
def save_close(app, workbook):
    workbook.save()
    workbook.close()
    app.quit()

def get_value_cmb(file_name_list):
    if file_name_list != None:
        list_value = []

        def go(*args):  # 处理事件，*args表示可变参数
            a = cmb.get()  # 返回选中的值
            list_value.append(a)

        root = Tk()
        root.title("请选择工作簿文件")
        root.geometry("300x200+10+20")
        cmb = ttk.Combobox(root)
        cmb.pack()
        cmb['value'] = file_name_list
        cmb.current(0)

        cmb.bind("<<ComboboxSelected>>", go)
        root.mainloop()
        return list_value[0]
    else:
        print("当前没有工作簿文件")

# 写入颜色值
def screening_data(new_file_name):
    app = xw.App(visible=True, add_book=False)

    # 1.打开原工作簿
    workbook = app.books.open(new_file_name)

    # 2.获取第1个工作表
    sheet = workbook.sheets[0]

    value_list_sheet = sheet.range(sheet.used_range.address).value[1:]
    first_value = sheet.range(sheet.used_range.address).value[0]
    for i in value_list_sheet:
        # 创建工作簿
        workbook = app.books.add()
        sheet = workbook.sheets[0]

        sheet.range("A1:I1").value = first_value
        sheet.range("A2:I2").value = i

        workbook.save(r"./新拆分工资条/" + i[2] + "_" + i[1] + ".xlsx")
        workbook.close()

        print(i[2] + "_" + i[1] + "已生成")

    # 3.保存工作簿
    # save_close(app,workbook)
    app.quit()
    app.kill()

# python程序执行入口
if __name__ == "__main__":
    path = "../source_material/08/03一键批量拆分工资条"
    os.chdir(path)
    # 1.先获取目录下的工作簿文件
    file_name_list = get_filename(".", ".xlsx")

    # 2.创建下拉了列表并返回所选择的值
    cmb_value = get_value_cmb(file_name_list)

    # 3.根据这个工作簿获取当前的工作表，默认是第一个工作表
    screening_data(cmb_value)
