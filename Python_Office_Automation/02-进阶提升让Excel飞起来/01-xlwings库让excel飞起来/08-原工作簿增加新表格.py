import xlwings as xw

app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open('../source_material/01/薪资表.xlsx')

# 打开工作表
sht = workbook.sheets['sheet1']

# 添加新工作表/可添加多个工作表
new_wb = workbook.sheets.add("奖金")
new_wb1 = workbook.sheets.add("年终奖")

# 在新工作表中写入数据
new_wb.range("A1").value = "奖金职工号"
new_wb1.range("A1").value = "年终奖职工号"

# 获取所有工作表
print(workbook.sheets)

# 另存为
workbook.save("../source_material/01/薪资表(4).xlsx")

# 关闭表
workbook.close()

# 关闭工作簿
app.quit()
