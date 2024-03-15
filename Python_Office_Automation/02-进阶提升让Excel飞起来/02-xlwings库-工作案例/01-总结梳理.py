"""
xlwings: import xlwings as xw
APP: app = xw.APP(visible=True,add_book=False)
Book:
    打开原工作簿:workbook=app.books.open('文件路径')
    打开新工作簿(未讲):workbook=app.books.add()
sheets:
    获取所有工作表:listsht=worksheets
    打开原有工作表:sht=workbook.sheets['sheet1']
    另一种方式:sht=workbook.sheets[下标]
range:
    获取指定范围表格:new_sht.range("A1").value
    给修改某一个表格:new_sht.range("A1").value="奖金"
    给修改某一行表格:new_sht.range("A1").value=列表
"""

# 导入模块
import xlwings as xw
# 创建实例，该实例是可以实现关闭excle
app = xw.App(visible=True, add_book=False)
# 打开工作簿
# workbook = app.books.open("../source_material/01/薪资表.xlsx")
# 创建新的工作簿
workbook = app.books.add()
# 打开工作表
worksheet = workbook.sheets['sheet1']
# 获取所有工作表
listsht = workbook.sheets
# 创建工作表
new_sht = workbook.sheets.add("奖金")
# 获取表格数据
print(new_sht.range("A1").value)
# 修改数据
new_sht.range("A1").value = "奖金001"
# 修改某一行数据
memlist = ['name', 'age', 'sex', 'tel']
new_sht.range("A2").value = memlist

# 保存工作簿
workbook.save("../source_material/01/薪资表(6).xlsx")
# 关闭工作表
workbook.close()
# 关闭工作簿
app.quit()
