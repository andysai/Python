"""
Font(字体)属性
    创建字体对象:font = xlwt.Font()
        font.name = "字体名称"
        font.blod = "是否加粗，True或者False"
        font.underline = "是否增加下划线，True或者False"
        font.italic = "是否为斜体，True或者False"
        font.escapement = xlwt.Font.ESCAPEMENT_NONE # escapement 字体效果
        # 常量值1:ESCAPEMENT_SUPERSCRIPT 字体悬空位于上方
        # 常量值2:ESCAPEMENT_SUBSCRIPT 字体悬空位于下方
        # 常量值3:ESCAPEMENT_NONE 字体没有这个效果

        font.colour_index = "字体颜色，参考素材库中的颜色值.jpg或者是使用列表xlwt.Style.colour_map"
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
font.italic = True
font.underline = True
font.escapement = xlwt.Font.ESCAPEMENT_NONE
# font.colour_index = 24
font.colour_index = xlwt.Style.colour_map['blue']

# 将设置好的属性赋值给style的对应的属性
style.font = font

new_sheet.write(1,1,'格式控制',style)

# 设置列宽
new_sheet.col(0)
# 设置行高
new_sheet.row(0).height_mismatch = True
new_sheet.row(0).height = 20 * 40

# 保存
new_workbook.save('../source_material/2019年某公司新资表(3).xls')