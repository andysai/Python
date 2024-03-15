"""
app = xw.App(visible=True,add_book=False)

visible表示实例是否可见
add_book表示是都新增Excle ，Ture表示新增，False表示不新增
"""
import xlwings as xw

app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open('../source_material/01/薪资表.xlsx')

# 打开工作表
sht = workbook.sheets['sheet1']

# 写入数据
newvalue = sht.range("B6:E10").value
listvalue = ['小张1', '男1', 29, '销售部经理']
sht.range("B6:E6").value = listvalue

# 另存为
workbook.save("../source_material/01/薪资表(3).xlsx")

# 关闭表
workbook.close()

# 关闭工作簿
app.quit()
