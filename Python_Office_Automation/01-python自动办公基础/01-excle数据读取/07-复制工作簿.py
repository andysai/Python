import xlrd
import xlwt
from xlutils.copy import copy

# 首先进行行读取
workbook = xlrd.open_workbook("../source_material/2019年某公司员工薪资表.xls", formatting_info = True)
sheet = workbook.sheets()[0]

# 进行复制
new_workbook = copy(workbook)
new_sheet = new_workbook.get_sheet(0)

# 保存
new_workbook.save("../source_material/2019年某公司员工薪资表(1).xls")