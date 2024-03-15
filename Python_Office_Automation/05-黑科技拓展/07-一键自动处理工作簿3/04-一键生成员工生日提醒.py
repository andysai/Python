import xlwings as xw
import time
from datetime import datetime
import os

# 获取指定后缀的文件
def get_filename(path, filetype):  # 输入路径、文件类型 例如'.csv'
    file_name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if filetype + ' ' in i + ' ':  # 这里后面不加一个字母可能会出问题，加上一个（不一定是空格）可以解决99.99%的情况
                file_name.append(i)
    return file_name  # 输出由有后缀的文件名组成的列表

# 1.读取信息
def read_sheet():
    list_value = []

    app = xw.App(visible=True, add_book=False)
    path = "../source_material/07/04一键生成员工生日提醒"
    os.chdir(path)
    # 先获取目录下的工作簿文件
    file_name = get_filename(".", ".xlsx")[0]

    # 1.打开原工作簿
    workbook = app.books.open(file_name)

    # 2.获取信息
    sheet = workbook.sheets[0]
    rows = int(sheet.used_range.address.split("$")[-1])
    for i in range(2, rows + 1):
        num_value = "D" + str(i)
        if sheet.range(num_value).value[0] != None:
            list_value.append(sheet.range(num_value).value)

    for time_value in list_value:
        time.sleep(0.4)
        month_value = time_value[10:12]
        day_value = time_value[12:14]

        d1 = datetime(datetime.now().year, int(month_value), int(day_value))

        d2 = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
        time_value_bir = (d1 - d2).days
        # print("第"+str(list_value.index(time_value)+2)+"___"+str(time_value_bir))
        num_value = "E" + str(list_value.index(time_value) + 2)
        if time_value_bir < 0:
            sheet_bir_value_str = "已过" + str(-time_value_bir) + "天"
            sheet.range(num_value).value = sheet_bir_value_str
            sheet.range(num_value).color = (184, 181, 252)
        else:
            sheet.range(num_value).value = str(time_value_bir)

            # 3.保存工作簿
    # save_close(app,workbook)

# 2.保存和退出程序
def save_close(app, workbook):
    workbook.save()
    workbook.close()
    app.quit()

# python程序执行入口
if __name__ == "__main__":
    # 执行写入代码
    read_sheet()
