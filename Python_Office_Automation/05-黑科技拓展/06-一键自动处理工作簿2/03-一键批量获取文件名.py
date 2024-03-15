# 导入标准库
import os
import re
import time
import xlwings as xw
from tkinter import *
import tkinter.font as tkFont

# 获取指定后缀的文件，比如获取文件第07章：序列-字典中所有的.mp4文件。
def get_filename(path, filetype):  # 输入路径、文件类型 例如'.csv'
    file_name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if filetype + ' ' in i + ' ':  # 这里后面不加一个字母可能会出问题，加上一个（不一定是空格）可以解决99.99%的情况
                file_name.append(i)
    return file_name  # 输出由有后缀的文件名组成的列表

# 写入数据
def set_gui():
    root = Tk()  # 创建TK对象
    root.title("输入数据")  # 设置标题
    root.geometry("380x80")  # 设置窗体大小
    entry = Entry(root, font=("Calibri", 20))
    entry.pack(side=LEFT)  # 设置输入框
    ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)

    def queding():
        get_value = entry.get()
        input_value(get_value)

    Button(root, text="确定", command=queding,
           font=ft,
           bg="yellow",
           width=10, height=2).pack(side=LEFT)

    root.mainloop()
# 写入数据
def input_value(get_value):
    path = "../source_material/06/03一键批量获取文件名/"
    os.chdir(path)
    namefile = "获取指定文件名"
    # 指定写入文件类型
    nameslist = get_filename(namefile, get_value)

    # 打开原有工作簿
    app = xw.App(visible=True, add_book=False)
    workbook = app.books.add()
    workbook.sheets.add("文件名")
    sheet = workbook.sheets["文件名"]
    # 循环写入数据
    for i in nameslist:
        print(i)
        sheet.range("A" + str(nameslist.index(i) + 1)).value = i

    save_close(app, workbook)

# 4.保存和退出程序
def save_close(app, workbook):
    workbook.save("文件名.xls")
    workbook.close()
    app.quit()

if __name__ == "__main__":
    # 输入后缀
    get_value = set_gui()
    print(get_value)
