"""
Alignment设置表格位置
    参数:
        HorizontalAlignment水平方向(左中右)
            右 -4152
            中 -4108
            左 -4131
        VerticalAlignment垂直方向(上中下)
            上 -4160
            中 -4108
            下 -4107
    语法:
        fg.api.HorizontalAlignment = -4152
        fg.api.VerticalAlignment = -4160
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

# 修改行高和列宽
fg.column_width = 13
fg.row_height = 60

# 水平居中
fg.api.HorizontalAlignment = -4108

# 垂直居中
fg.api.VerticalAlignment = -4108
