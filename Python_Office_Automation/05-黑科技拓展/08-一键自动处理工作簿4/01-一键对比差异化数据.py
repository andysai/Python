import xlwings as xw
import time
from datetime import datetime
import os
import random
from tkinter import *
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中

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

    # 2.获取所有工作表
    sheets = workbook.sheets
    dics_value = {}
    dics_letter = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"}

    for she in sheets:
        rows = she.used_range.address.split("$")[-1]
        columns = she.used_range.address.split("$")[-2]
        all_list_value = she.range(she.used_range.address).value
        for rows_value in all_list_value:
            for i in rows_value:
                if i != None and isinstance(i, float):
                    whith_row_num = str(all_list_value.index(rows_value) + 1)
                    whith_column_num = dics_letter.get(rows_value.index(i) + 1)
                    key_address = whith_column_num + whith_row_num
                    dics_value.setdefault(key_address, i)

    for key_outer, value_outer in dics_value.items():
        # 先把自己删除
        dics_value.pop(key_outer)

        for key_inner, value_inner in dics_value.items():
            if value_outer == value_inner:
                # 标注颜色
                color1 = random.randint(0, 255)
                color2 = random.randint(0, 100)
                color3 = random.randint(0, 250)
                she.range(key_inner).color = (color1, color2, color3)
                she.range(key_outer).color = (color1, color2, color3)

        # 在将自己添加
        dics_value.setdefault(key_outer, value_outer)

    # 3.保存工作簿
    # save_close(app,workbook)

# python程序执行入口
if __name__ == "__main__":
    path = "../source_material/08/01一键对比差异化数据"
    os.chdir(path)
    # 1.先获取目录下的工作簿文件
    file_name_list = get_filename(".", ".xlsx")

    # 2.创建下拉了列表并返回所选择的值
    cmb_value = get_value_cmb(file_name_list)

    # 3.根据这个工作簿获取当前的工作表，默认是第一个工作表
    screening_data(cmb_value)
