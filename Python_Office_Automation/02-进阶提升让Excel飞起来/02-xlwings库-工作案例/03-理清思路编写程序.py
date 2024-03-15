"""
需求:青海省全年有多少人获得多少的奖金？将获得奖金的全部放到另外一个新创建的青海省的表格中。
步骤:
    1.创建实例
    2.打开工作簿
    4.筛选并添加数据
        4.1 获取所有表格数据
        4.2 将筛选的数据存入列表
        4.3 列表数据加入新表格
    3.创建新的表格
    5.保存数据
    6.关闭工作表
    7.关闭工作簿
"""
# 导入模块
import xlwings as xw

# 创建实例
app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open("../source_material/02/华为奖励.xlsx")

# 筛选并添加数据
# 1.1 获取所有表格数据
sheets_list = workbook.sheets

# 1.2 将筛选的数据存入列表
# 创建一个空列表，用于存放数据
range_value_list = []
def readrange(excle):
    pass

for excle in sheets_list:
    readrange(excle)

# 1.3 列表数据加入新表格


# 新增工作表
qhs_excle = workbook.sheets.add("青海省")

# # 保存数据
# workbook.save("../source_material/02/华为奖励(1).xlsx")
#
# # 关闭工作表
# workbook.close()
#
# # 关闭工作簿
# app.quit()
