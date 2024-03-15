"""
设置列宽，256是1个衡量单位
worksheet.col(0).width = 256 * 20
worksheet.col(2).width = 256 * 20

设置行高，20是1个衡量单位
worksheet.row(0).height_mismatch = True
worksheet.row(0).height = 20 * 40
"""

# 导入读写模块
import xlrd
import xlwt
from xlutils.copy import copy

# 首先进行读取
workbook = xlrd.open_workbook('../source_material/2019年某公司新资表.xls', formatting_info=True)
sheet = workbook.sheet_by_index(0)

# 进行复制
new_workbook = copy(workbook)
new_sheet = new_workbook.get_sheet(0)
new_sheet.write(1,1,'格式控制')
# 设置列宽
new_sheet.col(0)
# 设置行高
new_sheet.row(0).height_mismatch = True
new_sheet.row(0).height = 20 * 40

# 保存
new_workbook.save('../source_material/2019年某公司新资表(1).xls')