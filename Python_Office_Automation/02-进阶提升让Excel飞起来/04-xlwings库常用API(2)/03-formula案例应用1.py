import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")
sheet = workbook.sheets[0]
sheet.activate()
fg = sheet.range("H15")

str_formula = ""
# 方法一:
# for i in range(5, 14, 2):
#     str_formula += "H" + str(i) + "+"
# 方法二:
for i in range(4, 15):
    if i%2 == 1:
        str_formula += "H" + str(i) + "+"

str_formula_new = str_formula[:-1]
str_formula_new1 = "=SUM(" + str_formula_new + ")"
fg.formula = str_formula_new1

