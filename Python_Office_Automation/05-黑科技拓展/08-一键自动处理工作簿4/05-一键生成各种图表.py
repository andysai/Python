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

# 创建图表
def screening_data(new_file_name):
    app = xw.App(visible=True, add_book=False)

    # 1.打开原工作簿
    workbook = app.books.open(new_file_name)

    # 2.获取所有工作表
    sheet = workbook.sheets[0]
    print(sheet.used_range.value)
    print(sheet.used_range.address)
    dic = {
        '3d_area': -4098,
        '3d_area_stacked': 78,
        '3d_area_stacked_100': 79,
        '3d_bar_clustered': 60,
        '3d_bar_stacked': 61,
        '3d_bar_stacked_100': 62,
        '3d_column': -4100,
        '3d_column_clustered': 54,
        '3d_column_stacked': 55,
        '3d_column_stacked_100': 56,
        '3d_line': -4101,
        '3d_pie': -4102,
        '3d_pie_exploded': 70,
        'area': 1,
        'area_stacked': 76,
        'area_stacked_100': 77,
        'bar_clustered': 57,
        'bar_of_pie': 71,
        'bar_stacked': 58,
        'bar_stacked_100': 59,
        'bubble': 15,
        'bubble_3d_effect': 87,
        'column_clustered': 51,
        'column_stacked': 52,
        'column_stacked_100': 53,
        'cone_bar_clustered': 102,
        'cone_bar_stacked': 103,
        'cone_bar_stacked_100': 104,
        'cone_col': 105,
        'cone_col_clustered': 99,
        'cone_col_stacked': 100,
        'cone_col_stacked_100': 101,
        'cylinder_bar_clustered': 95,
        'cylinder_bar_stacked': 96,
        'cylinder_bar_stacked_100': 97,
        'cylinder_col': 98,
        'cylinder_col_clustered': 92,
        'cylinder_col_stacked': 93,
        'cylinder_col_stacked_100': 94,
        'doughnut': -4120,
        'doughnut_exploded': 80,
        'line': 4,
        'line_markers': 65,
        'line_markers_stacked': 66,
        'line_markers_stacked_100': 67,
        'line_stacked': 63,
        'line_stacked_100': 64,
        'pie': 5,
        'pie_exploded': 69,
        'pie_of_pie': 68,
        'pyramid_bar_clustered': 109,
        'pyramid_bar_stacked': 110,
        'pyramid_bar_stacked_100': 111,
        'pyramid_col': 112,
        'pyramid_col_clustered': 106,
        'pyramid_col_stacked': 107,
        'pyramid_col_stacked_100': 108,
        'radar': -4151,
        'radar_filled': 82,
        'radar_markers': 81,
        'xy_scatter': -4169,
        'xy_scatter_lines': 74,
        'xy_scatter_lines_no_markers': 75,
        'xy_scatter_smooth': 72,
        'xy_scatter_smooth_no_markers': 73}
    w = 385
    h = 241
    n = 0
    x = 10
    y = 10
    for i in dic.keys():
        xx = x + n % 2 * w  # 用来生成图表放置的x坐标。
        yy = y + n // 2 * h  # 用来生成图表放置的y坐标。
        chart = sheet.charts.add(xx, yy)
        chart.set_source_data(sheet.used_range.expand())
        chart.chart_type = i
        chart.api[1].ChartTitle.Text = i
        n += 1

    time.sleep(10)
    save_close(app, workbook, new_file_name)

# 2.保存和退出程序
def save_close(app, workbook, new_file_name):
    workbook.save(new_file_name[:-4] + "__图表.xlsx")
    workbook.close()
    app.quit()

# python程序执行入口
if __name__ == "__main__":
    path = "../source_material/08/05一键生成各种图表"
    os.chdir(path)
    # 1.先获取目录下的工作簿文件
    file_name_list = get_filename(".", ".xlsx")
    # 2.创建下拉了列表并返回所选择的值
    cmb_value = get_value_cmb(file_name_list)
    # 3.根据这个工作簿获取当前的工作表，默认是第一个工作表
    screening_data(cmb_value)
    # 已经生成图标
    print("已经生成图表")
