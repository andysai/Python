import xlwings as xw

app = xw.App(visible=True, add_book=False)

# 创建工作簿
workbook = app.books.add()

# 打开工作表
sht = workbook.sheets['sheet1']

# 在新工作表中写入数据
sht.range("A1").value = "职工号"

workbook.save('./test.xlsx')

workbook.close()
app.quit()
