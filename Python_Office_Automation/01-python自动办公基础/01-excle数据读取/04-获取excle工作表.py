# 导入模块
import xlrd

# 获取工作簿:1.文件路径(全名称) 2.字符串 3.字符串转义 4.变量
workbook = xlrd.open_workbook("../source_material/2019年某公司员工薪资表.xls", formatting_info=True)

# 获取工作表:
# 方法一:
sheet1 = workbook.sheet_by_index(0)
# 方法二:
sheet2 = workbook.sheet_by_name("Sheet1")
# 方法三:
sheet3 = workbook.sheets()[0]
print(sheet2)
