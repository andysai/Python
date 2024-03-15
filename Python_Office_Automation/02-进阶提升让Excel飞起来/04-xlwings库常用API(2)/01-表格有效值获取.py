"""
选择方格数量
    fg=sheet.range("A1"B13")
    fg.count
    获取当前有效区域对象
    fg.autofit
    fg.current_region
    以列表打印选择区域的数据
    fg.current_region.value
"""
import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")
sheet = workbook.sheets[0]
sheet.activate()

fg = sheet.range("A1:B13")
# print(fg.count)
# print(fg.autofit)
print(fg.current_region.value)
