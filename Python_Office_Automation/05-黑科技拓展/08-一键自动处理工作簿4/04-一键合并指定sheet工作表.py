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

    # 2.获取所有工作表
    sheet_name_list = []
    sheets = workbook.sheets
    for she in sheets:
        sheet_name_list.append(she.name)
    # 关闭工作簿
    # save_close(app,workbook)
    # 复制这个工作簿
    file = open(new_file_name, "rb")
    str_file = file.read()
    file.close()

    # 写入文件
    new_file_name2 = "新合并—" + new_file_name[:-5] + ".xlsx"
    f = open(new_file_name2, "wb")
    f.write(str_file)
    f.close()

    # 关闭工作表
    workbook.save()
    workbook.close()

    # 创建复选框
    root = Tk()
    root.title("请选择工作簿文件")
    root.geometry("300x400+10+20")
    dict_num = {}
    for i in sheet_name_list:
        dict_num.setdefault(i, StringVar())
        Checkbutton(root, text=i, variable=dict_num[i], ).pack(anchor=W)

    ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)

    # 3.打开新工作簿
    workbook = app.books.open(new_file_name2)
    sheet_list = workbook.sheets

    def queding():
        for key, value in dict_num.items():
            # print(key,value.get())
            if value.get() == str(0):
                # 删除工作簿
                sheet_list[key].delete()
                print(key + "已删除")
        save_close(app, workbook)

    Button(root, text="确定", command=queding,
           font=ft,
           bg="yellow",
           width=6, height=1).pack(side=LEFT)
    mainloop()

    for she_name in sheet_name_list:
        range_value = "A"+str(sheet_name_list.index(she_name)+1)
        sheet_rangs = workbook.sheets["目录"].range(range_value)
        sheet_rangs.value = she_name
        sheet_rangs.add_hyperlink("#"+she_name+"!B2",
                                  text_to_display=she_name,
                                  screen_tip=she_name)
    #创建一个按钮，按钮点击的时候就返回到第一个工作表
    root = Tk() #创建TK对象
    root.title("返回") #设置标题
    root.geometry("300x80")#设置窗体大小
    ft = tkFont.Font(family='Fixdsys', size=30, weight=tkFont.BOLD)
    def queding():
        sheets[0].activate()
    Button(root,text = "返回",command = queding,
           font = ft,
           bg = "yellow",
           width=10,height=4).pack()

    #3.保存工作簿
    #save_close(app,workbook)


# python程序执行入口
if __name__ == "__main__":
    path = "../source_material/08/04一键合并指定sheet工作表"
    os.chdir(path)
    # 1.先获取目录下的工作簿文件
    file_name_list = get_filename(".", ".xlsx")

    # 2.创建下拉了列表并返回所选择的值
    cmb_value = get_value_cmb(file_name_list)

    # 3.根据这个工作簿获取当前的工作表，默认是第一个工作表
    screening_data(cmb_value)

    # wb.sheets['目录'].range('A' + str(shtNum + 1)).add_hyperlink(str('#' + shtList[shtNum] + '!A1'),
    # shtList[shtNum],shtList[shtNum])
