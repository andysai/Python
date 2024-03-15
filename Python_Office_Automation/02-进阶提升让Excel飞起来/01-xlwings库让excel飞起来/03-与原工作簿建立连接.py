# 导入模块并命名
import xlwings as xw

# 优先使用相对路径打开工作簿
wb = xw.Book('../source_material/01/薪资表.xlsx')

# 获取表格数据
sht = wb.sheets["sheet1"]

# 修改数据
# sht.range("A1").value = "职工"

#追加数据
sht.range("A1").value = sht.range("A1").value + "003"

# 保存
# wb.save()

# 另存为
# wb.save("../source_material/01/薪资表(1).xlsx")

# 关闭表
wb.close()