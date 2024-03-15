import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")
sheet = workbook.sheets[0]
sheet.activate()
fg = sheet.range("H15")
singular = []
sum_singular = 0
for i in range(4,15):
    fg_address = "H" + str(i)
    if int(sheet.range(fg_address).value)%2 == 1:
        sum_singular += int(sheet.range(fg_address).value)

fg.value = sum_singular
