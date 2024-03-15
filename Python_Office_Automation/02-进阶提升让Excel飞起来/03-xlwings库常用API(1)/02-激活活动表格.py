"""
激活活动表格
    # 打开表格
    sheet = workbook.sheets[4]
    # 设置活动表格
    sheet.activate()
"""
# 导入模块
import xlwings as xw
# 创建实例
app = xw.App(visible=True, add_book=False)
# 打开工作簿
workbook = app.books.open('../source_material/03/2019年某公司员工薪资表.xls')

# 新建一个表格
workbook.sheets.add("奖金")

# 激活表格--设置表格为活动表格
sheet = workbook.sheets[4]
sheet.activate()