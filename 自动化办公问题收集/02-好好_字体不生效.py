# 可能和office版本有关系

# 导入模块
import xlrd
import xlwt
from xlutils.copy import copy
# 打开工作簿
workbook = xlrd.open_workbook(r"E:\study\python\Python_Office_Automation\01-python自动办公基础\source_material\2019年某公司员工薪资表.xls", formatting_info = True)
# 打开工作表
sheet = workbook.sheets()[0]

# 进行复制
new_workbook = copy(workbook)
new_sheet = new_workbook.get_sheet(0)

# 设置字体属性
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = "隶书"
font.bold = True
font.height = 20*40
font.italic = True
# font.escapement = xlwt.Font.ESCAPEMENT_NONE

style.font = font


new_sheet.write(1, 1, "格式控制", style)
new_sheet.col(0).width = 256 * 20
new_sheet.row(0).height_mismatch = True
new_sheet.row(0).height = 20 * 40

new_workbook.save(r"E:\study\python\Python_Office_Automation\01-python自动办公基础\source_material\2019年某公司员工薪资表(2).xls")
