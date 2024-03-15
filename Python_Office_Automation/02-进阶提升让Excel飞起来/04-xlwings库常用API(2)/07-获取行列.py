"""
获取有有效区域的范围(行和列)
方式1：
    获取行和列的值：sheet.used_range.address.split("$")
    获取有多少行：sheet.used_range.address.split("$")[-1]
    获取到哪个列：sheet.used_range.address.split("$")[-2]
方式2：
sheet.used_range.shape
返回一个元组， 这个元组也可以看出有多少行多少列，比如（12,10）这个就表示12行，10列
"""
import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")
sheet = workbook.sheets[0]
sheet.activate()
# 获取行和列的值
# sht = sheet.used_range.address.split("$")

# 获取有多少行：
sht2 = sheet.used_range.address.split("$")[-1]
print(sht2)
# 获取到哪个列：
sht = sheet.used_range.address.split("$")[-2]
print(sht)

sht3 = sheet.used_range.shape
print(sht3)