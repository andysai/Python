"""
XFStyle风格样式:
    Font(字体)
    Borders(边界)
    Alignment(对齐)
    Pattern(模式)

XFStyle语法:
    初始化样式
    xlwt.XFSytle()
    创建属性对象
    xlwt.Font()
    对属性的值进行初始化
    font.name # 字体名称，设置任意字体
    font.blod # 是否加粗
    font.height # 字号*20
    将设置号的属性对象赋值黑style的对应的属性
    style.font = font
    写入表数据的时候调用style对象即可
    worksheet.write(1,1,style)
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

# 初始化样式
style = xlwt.XFStyle()
# 创建属性对象麦哲伦使用字体属性当做例子说明
font = xlwt.Font()

# 对属性的值进行初始化
font.name = '宋体'
font.bold = True
font.height = 20 * 20

# 将设置好的属性赋值给style的对应的属性
style.font = font

new_sheet.write(1,1,'格式控制',style)

# 设置列宽
new_sheet.col(0)
# 设置行高
new_sheet.row(0).height_mismatch = True
new_sheet.row(0).height = 20 * 40

# 保存
new_workbook.save('../source_material/2019年某公司新资表(2).xls')