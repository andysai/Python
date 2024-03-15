"""
Borders边界设置
    参数:
        5表示从左上角到右下角
        6表示从左下角到右上角
        7左部边框
        8顶部边框
        9底部边框
        10右部边框
        11内部垂直边框
        12内部水平边框

    线的风格:LineStyle
    线的粗细:Weight
    语法:
        # fg方格或者方格范围，左边有边框，边框风格为1
        fg.api.Borders(参数).LineStyle = 1
        # fg方格或者方格范围，左边有边框，边框粗细为1
        fg.api.Borders(参数).Weight = 1
"""
# 导入模块
import xlwings as xw

# 创建实例
app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xlsx")

# 打开工作表
worksheet = workbook.sheets['sheet1']

# 获取方格区域
fg = worksheet.range("B1:H6")

# 设置边框和粗细
# 上边框
# fg.api.Borders(8).LineStyle = 1
# fg.api.Borders(8).Weight = 2

# 下边框
# fg.api.Borders(9).LineStyle = 1
# fg.api.Borders(9).Weight = 2

# 左边框
# fg.api.Borders(7).LineStyle = 1
# fg.api.Borders(7).Weight = 3

# 右边框
# fg.api.Borders(10).LineStyle = 1
# fg.api.Borders(10).Weight = 2

# 对角
# fg.api.Borders(5).LineStyle = 1
# fg.api.Borders(5).Weight = 2
# fg.api.Borders(6).LineStyle = 1
# fg.api.Borders(6).Weight = 2

# 垂直
# fg.api.Borders(11).LineStyle = 1
# fg.api.Borders(11).Weight = 2

# 水平
# fg.api.Borders(12).LineStyle = 1
# fg.api.Borders(12).Weight = 2


