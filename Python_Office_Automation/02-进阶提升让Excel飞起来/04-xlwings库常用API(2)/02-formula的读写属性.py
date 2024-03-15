"""
获取方格计算公式
    fg = sheet.range("H15") # 选择区域
    fg.formula = '=SUM(H6:H14)'

"""
import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")
sheet = workbook.sheets[0]
sheet.activate()
fg = sheet.range("H15")

print(type(fg.formula))
fg.formula = '=SUM(H6:H14)'

