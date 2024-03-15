# coding:utf-8
import xlrd
import os
import xlwt
from xlutils.copy import copy

# 需要安装pip install xlrd   pip install xlwt  pip install xlutils

def get_allfile_msg(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return root, dirs, [file for file in files if file.endswith('.xls') or file.endswith('.xlsx')]


def get_allfile_url(root, files):
    allFile_url = []
    for file_name in files:
        file_url = root + '/' + file_name
        allFile_url.append(file_url)
    return allFile_url

def all_to_one(root, allFile_url, file_name='allExcel.xls', title=None, have_title=True):
    # 首先在该目录下创建一个excel文件,用于存储所有excel文件的数据
    file_name = root + '/' + file_name
    create_excel(file_name, title)

    list_row_data = []
    for f in range(0, len(allFile_url)):
        # for f in allFile_url:
        # 打开excel文件
        print('打开%s文件' % allFile_url[f])
        excel = xlrd.open_workbook(allFile_url[f])
        # 根据索引获取sheet，这里是获取第一个sheet
        table = excel.sheet_by_index(0)
        print('该文件行数为：%d，列数为：%d' % (table.nrows, table.ncols))

        # 获取excel文件所有的行
        for i in range(table.nrows):
            # yezi表头修改处，如果表头是2行则为2，1行则为1
            if have_title and i < top and f != 0:
                continue
            else:
                row = table.row_values(i)  # 获取整行的值，返回列表
                list_row_data.append(row)

    print('总数据量为%d' % len(list_row_data))
    # 写入all文件
    add_row(list_row_data, file_name)

# 创建文件名为file_name,表头为title的excel文件
def create_excel(file_name, title):
    print('创建文件%s' % file_name)
    a = xlwt.Workbook()
    # 新建一个sheet
    table = a.add_sheet('sheet1', cell_overwrite_ok=True)
    # 写入数据
    # for i in range(len(title)):
    #    table.write(0, i, title[i])
    a.save(file_name)

# 向文件中添加n行数据
def add_row(list_row_data, file_name):
    # 打开excel文件
    allExcel1 = xlrd.open_workbook(file_name)
    sheet = allExcel1.sheet_by_index(0)
    # copy一份文件,准备向它添加内容
    allExcel2 = copy(allExcel1)
    sheet2 = allExcel2.get_sheet(0)

    # 写入数据
    i = 0
    for row_data in list_row_data:
        for j in range(len(row_data)):
            sheet2.write(sheet.nrows + i, j, row_data[j])
        i += 1
    # 保存文件，将原文件覆盖
    allExcel2.save(file_name)
    print('合并完成')

if __name__ == '__main__':
    # 设置文件夹路径，
    file_dir = r'.\excel'
    # 模板顶部表头行数，有几行就写几行
    top = 2
    # 设置合并之后文件的名字
    file_name = '合并表格.xls'

    # 获取文件夹的路径,该路径下的所有文件夹，以及所有文件
    root, dirs, files = get_allfile_msg(file_dir)
    # 拼凑目录路径+文件名,组成文件的路径,用一个列表存储
    allFile_url = get_allfile_url(root, files)

    # have_title参数默认为True,为True时不读取excel文件的首行
    all_to_one(root, allFile_url, file_name=file_name, title=None, have_title=True)
