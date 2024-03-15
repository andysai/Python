# 导入模块
import xlrd

# 获取工作簿:1.文件路径(全名称) 2.字符串 3.字符串转义 4.变量
workbook = xlrd.open_workbook("../source_material/2019年某公司员工薪资表.xls", formatting_info=True)
