# 导入模块并命名
import xlwings as xw

# 优先使用相对路径打开工作簿
wb = xw.Book('../source_material/01/薪资表.xlsx')

# 获取表格数据
sht = wb.sheets["sheet1"]

newvalue = sht.range("B6:E10").value

# 修改数据
listvalue = ['张明','男',35,'销售部']
sht.range("B6:E6").value = listvalue

# 另存为
wb.save("../source_material/01/薪资表(2).xlsx")

# 关闭表
wb.close()