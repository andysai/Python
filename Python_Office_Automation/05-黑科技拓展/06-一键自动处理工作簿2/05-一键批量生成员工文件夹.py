import xlwings as xw
import os

# 1.读取信息
def read_sheet():
    list_value = []

    app = xw.App(visible=True, add_book=False)

    # 1.打开原工作簿
    workbook = app.books.open("../source_material/06/05一键批量生成员工文件夹/职员信息表.xlsx")

    # 2.获取信息
    sheet = workbook.sheets[0]
    rows = int(sheet.used_range.address.split("$")[-1])
    for i in range(2, rows + 1):
        num_value = "A" + str(i)
        if sheet.range(num_value).value[0] != None:
            list_value.append(sheet.range(num_value).value)

    # 3.保存工作簿
    save_close(app, workbook)
    return list_value


# 2.将获取列表的值创建新的文件
def set_worker_file(path, list_info):
    for worker_name in list_info:
        path = path.strip()
        isExists = os.path.exists(path + worker_name)
        print("正在努力创建中...")

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path + worker_name)
            print(worker_name + ' 文件夹已创建')

        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(worker_name + '文件夹已存在')


# 4.保存和退出程序
def save_close(app, workbook):
    workbook.save()
    workbook.close()
    app.quit()

# python程序执行入口
if __name__ == "__main__":
    path = "../source_material/06/05一键批量生成员工文件夹/员工文件夹/"

    # 1.读取表格信息
    list_info = read_sheet()

    # 2.将获取列表的值创建新的文件
    set_worker_file(path, list_info)
