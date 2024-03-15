"""
Borders(边界)属性
    创建边界对象:创建字体对象:borders=xlwt.Boeders()
        borders.top = 2 # 上边框，数字为像素单位，数字越大表示线越粗
        borders.bottom = 2 # 下边框
        borders.left = 2 # 左边框
        borders.right = 2 # 右边框
        xlwt.Borders.THIN # 如果数字为1，可以使用xlwt.Borders.THIN来表示
        borders.left_colour = 33 # 边框左边颜色，参考素材库中的颜色值.jpg或者是使用列表xlwt.Style.colour_map
        borders.right_colour = 33 # 边框右边颜色
        borders.top_colour = 33 # 边框顶部颜色
        borders.buttom_colour = 33 # 边框底部颜色
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

# 创建边界对象:创建字体对象
borders = xlwt.Borders()
borders.top = 2  # 上边框，数字为像素单位，数字越大表示线越粗
borders.bottom = 2  # 下边框
borders.left = 2  # 左边框
borders.right = 2  # 右边框

borders.left_colour = 24  # 边框左边颜色，参考素材库中的颜色值.jpg或者是使用列表xlwt.Style.colour_map
borders.right_colour = 24  # 边框右边颜色
borders.top_colour = 24  # 边框顶部颜色
borders.buttom_colour = 24  # 边框底部颜色

# 将设置好的属性赋值给style的对应的属性
style.borders= borders

new_sheet.write(1,1,'格式控制',style)

# 设置列宽
new_sheet.col(0)
# 设置行高
new_sheet.row(0).height_mismatch = True
new_sheet.row(0).height = 20 * 40

# 保存
new_workbook.save('../source_material/2019年某公司新资表(4).xls')