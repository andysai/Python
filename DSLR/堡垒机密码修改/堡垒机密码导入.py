# coding=utf-8

# 导入模块
import xlwings as xw
import csv
import datetime

# 新建表格
app = xw.App(visible=True, add_book=False)
workbook = app.books.add()

# 获取表格数据
sht = workbook.sheets["sheet1"]

# 写入表头数据
A1_head = sht.range("A1:N1")
A1_values = ['主机IP', '主机名称', '操作系统', '主机编码', '帐户登录名', '帐户密码', '协议:端口', 'Oracle数据库', 'Oracle登录属性',
             'Oracle连接为', 'DB2资产列表', '主机组名称', '备注', '主机网络']
A1_head.value = A1_values


# rhel5主机数据匹配
with open('虚拟机ip地址/rhel5.txt') as f:
    rhel5_list = f.readlines()
    rhel5_lists = []
    for i in rhel5_list:
        rhel5_lists.append(i.strip())

# rhel6主机数据匹配
with open('虚拟机ip地址/rhel6.txt') as f:
    rhel6_list = f.readlines()
    rhel6_lists = []
    for i in rhel6_list:
        rhel6_lists.append(i.strip())

# ubuntu 10.12.12.71不能改密码
with open('虚拟机ip地址/ubuntu.txt') as f:
    ubuntu_list = f.readlines()
    ubuntu_lists = []
    for i in ubuntu_list:
        ubuntu_lists.append(i.strip())

# suse11主机数据匹配
with open('虚拟机ip地址/suse11.txt') as f:
    suse11_list = f.readlines()
    suse11_lists = []
    for i in suse11_list:
        suse11_lists.append(i.strip())


# centos6_list主机数据匹配
with open('虚拟机ip地址/centos6.txt') as f:
    centos6_list = f.readlines()
    centos6_lists = []
    for i in centos6_list:
        centos6_lists.append(i.strip())

# centos7_list主机数据匹配
with open('虚拟机ip地址/centos7.txt') as f:
    centos7_list = f.readlines()
    centos7_lists = []
    for i in centos7_list:
        centos7_lists.append(i.strip())

# 查询到的数据添加到列表
file_name = '20220321172021479624_276840.csv'
with open(file_name, encoding='utf-8') as f:
    f_csv = csv.reader(f)
    first_A = []
    for row in f_csv:
        if row[0] in rhel5_lists and row[4] == 'root':
            first_A.append(row)
        if row[0] in rhel6_lists and row[4] == 'root':
            first_A.append(row)
        if row[0] in ubuntu_lists and row[4] == 'root':
            first_A.append(row)
        if row[0] in suse11_lists and row[4] == 'root':
            first_A.append(row)
        if row[0] in centos6_lists and row[4] == 'root':
            first_A.append(row)
        if row[0] in centos7_lists and row[4] == 'root':
            first_A.append(row)
# 导入数据
row_num = len(first_A)
for i in range(0, row_num):
        str_address_first = "A" + str(i+2) + ":" + "N" + str(i+2)
        sht.range(str_address_first).value = first_A[i]

# 修改密码列数据
row_num = len(first_A)
password = 'Dslr*2022!@#'
for i in range(0, row_num):
        F_l = "F" + str(i+2) + ":" + "F" + str(i+2)
        sht.range(F_l).value = password

# 另存为
date = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" \
       + str(datetime.datetime.now().day)
save_filename = r"D:\study\DSLR\堡垒机密码修改\堡垒机密码导入" + date + ".xlsx"
workbook.save(save_filename)

# 关闭表
workbook.close()

# 关闭工作簿
app.quit()
