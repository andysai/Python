import xlwings as xw
from tkinter import *
import re

# 执行拆分功能
def chaifen(app, workbook, save_file_path):
    # 获取所有的工作表
    for sheet in workbook.sheets:
        newsave_file_path = save_file_path + sheet.name + ".xls"
        workbooks = app.books.add()
        workbooks.save(newsave_file_path)

        # 写入数据
        new_workbook = app.books.open(save_file_path + sheet.name + ".xls")
        print("正在写入...")
        new_str_address = re.sub(r"\$", "", str(sheet.used_range.address))
        new_workbook.sheets[0].range(new_str_address).value = sheet.used_range.value
        new_workbook.save()
        new_workbook.close()
        print(newsave_file_path + "已完成写入")

# 4.保存和退出程序
def save_close(app, workbook):
    workbook.save()
    workbook.close()
    app.quit()

# python程序执行入口
if __name__ == "__main__":
    # 打开原有工作簿
    app = xw.App(visible=True, add_book=False)
    workbook = app.books.open("../source_material/06/01一键拆分个工作簿/拆分工作簿.xlsx")
    save_file_path = "../source_material/06/01一键拆分个工作簿/拆分工作簿/"

    # 2.执行拆分
    chaifen(app, workbook, save_file_path)

    # 3.保存工作簿
    save_close(app, workbook)
