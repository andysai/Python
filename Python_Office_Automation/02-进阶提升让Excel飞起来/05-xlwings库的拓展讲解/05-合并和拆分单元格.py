"""
合并拆分单元格
    合并单元格
        sheet.range("A1:B2").api.Merge()
    拆分单元格
        sheet.range("A1").api.UnMerge()
"""
# 导入模块
import xlwings as xw

# 创建实例
app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xlsx")

# 打开工作表
worksheet = workbook.sheets['sheet2']
worksheet.activate()

# 合并单元格
# worksheet.range("A1:B2").api.Merge()

# 拆分单元格
worksheet.range("A1").api.UnMerge()


