# coding=utf-8

# 导入模块
import xlwings as xw
import datetime
import openpyxl

# 新建表格
app = xw.App(visible=True, add_book=False)
workbook = app.books.add()

# 获取表格数据
sht = workbook.sheets["sheet1"]

A1_head = sht.range("A1:N1")
A1_values = ['系统版本', 'IP', '账号', '密码', '应用名称', '状态', '虚拟化平台', '备注']
A1_head.value = A1_values

# 打开一个Workbook对象
wb = openpyxl.load_workbook('虚拟机资源统-2022-03-22计.xlsx')
sheets = wb.worksheets

# 获取第一张sheet
sheet1 = sheets[0].values
row1 = []
for row in sheet1:
    row1.append(list(row))

# rhel5主机数据匹配
with open('虚拟机ip地址/rhel5.txt', 'r') as f:
    rhel5_list = f.readlines()
    rhel5_lists = []
    for i in rhel5_list:
        rhel5_lists.append(i.strip())

# rhel6主机数据匹配
with open('虚拟机ip地址/rhel6.txt', 'r') as f:
    rhel6_list = f.readlines()
    rhel6_lists = []
    for i in rhel6_list:
        rhel6_lists.append(i.strip())

# ubuntu 10.12.12.71不能改密码
with open('虚拟机ip地址/ubuntu.txt', 'r') as f:
    ubuntu_list = f.readlines()
    ubuntu_lists = []
    for i in ubuntu_list:
        ubuntu_lists.append(i.strip())

# suse11主机数据匹配
with open('虚拟机ip地址/suse11.txt', 'r') as f:
    suse11_list = f.readlines()
    suse11_lists = []
    for i in suse11_list:
        suse11_lists.append(i.strip())


# centos6_list主机数据匹配
with open('虚拟机ip地址/centos6.txt', 'r') as f:
    centos6_list = f.readlines()
    centos6_lists = []
    for i in centos6_list:
        centos6_lists.append(i.strip())

# centos7_list主机数据匹配
with open('虚拟机ip地址/centos7.txt', 'r') as f:
    centos7_list = f.readlines()
    centos7_lists = []
    for i in centos7_list:
        centos7_lists.append(i.strip())

# 统计能匹配上的数据
list_A = []
for i in row1:
    if i[1] in rhel5_lists and i[2] == 'root' and i[5] == '正常':
        i[3] = 'Dslr*2022!@#'
        list_A.append(i)
    elif i[1] in rhel6_lists and i[2] == 'root' and i[5] == '正常':
        i[3] = 'Dslr*2022!@#'
        list_A.append(i)
    elif i[1] in ubuntu_lists and i[2] == 'root' and i[5] == '正常':
        i[3] = 'Dslr*2022!@#'
        list_A.append(i)
    elif i[1] in suse11_lists and i[2] == 'root' and i[5] == '正常':
        i[3] = 'Dslr*2022!@#'
        list_A.append(i)
    elif i[1] in centos6_lists and i[2] == 'root' and i[5] == '正常':
        i[3] = 'Dslr*2022!@#'
        list_A.append(i)
    elif i[1] in centos7_lists and i[2] == 'root' and i[5] == '正常':
        i[3] = 'Dslr*2022!@#'
        list_A.append(i)
    else:
        if i[0] != '系统版本':
            list_A.append(i)

# 统计行数
list_he = len(list_A)

# 导入修改完密码的数据
for i in range(0, len(list_A)):
        str_address_first = "A" + str(i+2) + ":" + "H" + str(i+2)
        sht.range(str_address_first).value = list_A[i]

# 另存为
date = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" \
       + str(datetime.datetime.now().day)
save_filename = r"D:\study\DSLR\堡垒机密码修改\虚拟机资源表" + date + ".xlsx"
workbook.save(save_filename)

# 关闭表
workbook.close()

# 关闭工作簿
app.quit()
