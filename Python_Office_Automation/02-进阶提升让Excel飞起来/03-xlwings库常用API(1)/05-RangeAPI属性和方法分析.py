"""
range常用API
    获取指定方格的值:
        range("A1").value
    获取指定方格范围的值:
        range("A1:D4").value
"""
import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")
sheet = workbook.sheets[0]

fg = sheet.range("A1")


for i in dir(fg):
    print(i)


app.quit()