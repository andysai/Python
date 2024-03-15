# 导入模块
import xlrd

# 获取工作簿:1.文件路径(全名称) 2.字符串 3.字符串转义 4.变量
workbook = xlrd.open_workbook("../source_material/2019年某公司员工薪资表.xls", formatting_info=True)

# 获取工作表:
# 方法一:
sheet1 = workbook.sheet_by_index(0)
# 方法二:
# sheet2 = workbook.sheet_by_name("Sheet1")
# 方法三:
# sheet3 = workbook.sheets()[0]

# 获取工作表中的某一个表格数据
# cellvalue = sheet1.cell_value(rowx = 2,colx = 1)
# cellvalue = sheet1.cell(2,1).value
# print(cellvalue)

"""
需求:获取工作表中的某一行或某一列的数据
    1.获取总行数nrows
    2.获取总列数nclos
    3.获取对应的行
    4.获取对应的列
"""

r_num = sheet1.nrows
c_num = sheet1.ncols
print(r_num, c_num)
print(sheet1.row(0))
# print(sheet1.col(0))
# print(f'一共有{r_num}行,{c_num}列')
# 获取工作表中的所有数据
# 打印行
# for i in range(sheet1.nrows):
#     print(sheet1.row(i))

# 打印列
# for i in range(sheet1.ncols):
#     print(sheet1.col(i))

# 打印指定的行和列
# for i in range(r_num):
#     for j in range(c_num):
#         row = 2
#         col = 1
#         if row == i and col == j:
#             print(sheet1.cell(row,col).value)
