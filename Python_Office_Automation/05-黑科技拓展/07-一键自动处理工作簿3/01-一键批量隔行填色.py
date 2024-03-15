import xlwings as xw
from tkinter import *
import tkinter.font as tkFont
import os

# 写入数据
def set_gui(new_file_name):
    root = Tk()  # 创建TK对象
    root.title("输入要填充的颜色值")  # 设置标题
    root.geometry("380x80")  # 设置窗体大小
    entry = Entry(root, font=("Calibri", 20))
    entry.pack(side=LEFT)  # 设置输入框
    ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)

    def queding():
        get_value = entry.get()
        input_value(get_value, new_file_name)

    Button(root, text="确定", command=queding,
           font=ft,
           bg="yellow",
           width=10, height=2).pack(side=LEFT)

    root.mainloop()

# 写入颜色值
def input_value(get_value, new_file_name):
    app = xw.App(visible=True, add_book=False)

    # 1.打开原工作簿
    workbook = app.books.open(new_file_name)

    # 2.获取所有工作表
    sheets = workbook.sheets
    n = 0
    for she in sheets:
        n += 1
        rows_num = she.used_range.address.split("$")[-1]
        culomn_num = she.used_range.address.split("$")[3]
        range_value = "A" + str(n) + ":" + culomn_num + str(n)

        color_list = get_value.split(",")
        new_color_list = []
        for i in color_list:
            new_color_list.append(int(i))
        new_color_list = tuple(new_color_list)

        # 填充颜色
        for culomn in range(0, int(rows_num) + 1):
            range_value_new = "A" + str(culomn) + ":" + culomn_num + str(culomn)
            if culomn % 2 == 1:
                she.range(range_value_new).color = new_color_list

                # 3.保存工作簿
    save_close(app, workbook)

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

def read_write_file(file_name):
    # 读取文件
    file = open(file_name, "rb")
    str_file = file.read()
    file.close()

    # 写入文件
    new_file_name = "隔行填色" + file_name[:-5] + ".xlsx"
    f = open(new_file_name, "wb")
    f.write(str_file)
    f.close()
    return new_file_name

# python程序执行入口
if __name__ == "__main__":
    path = "../source_material/07/01一键批量隔行填色"
    os.chdir(path)
    # 1.先复制原工作簿
    file_name = get_filename(".", ".xlsx")[0]
    new_file_name = read_write_file(file_name)

    # 2.获取颜色数据
    get_value = set_gui(new_file_name)
