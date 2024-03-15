"""
清除活动表格
    sheet = workbook.sheets[0]
    清除表格的内容和格式
        sheet.clear()
    清除表格内容
        sheet.clear_contents()
    删除表格
        sheet.delete()
"""
import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")
sheet = workbook.sheets[0]
# list1 = dir(sheet)
# for i in list1:
#     print(i)
# help(sheet)
print(xw.__file__)
# sheet1 = workbook.sheets[0]
# sheet1.clear_contents()
# sheet1 = workbook.sheets[0]
# sheet1.clear()
# sheet1 = workbook.sheets[2]
# sheet1.delete()
app.quit()