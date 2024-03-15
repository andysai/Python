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
    for i in range(2, 100):
        # 组合字符
        # 获取单个单元格
        str_sheet = "E" + str(i)
        # 获取行
        str_sheet1 = "A" + str(i) + ":" + "E" + str(i)
        # 获取E列的值
        str_value = excle.range(str_sheet).value
        # 判断是否是青海省
        if str_value == "青海省":
            str_sheet_row = excle.range(str_sheet1).value
            range_value_list.append(str_sheet_row)

# 获取每个表格的名称
for excle in sheets_list:
    readrange(excle)

# 新增工作表
qhs_excle = workbook.sheets.add("青海省")

# 1.3 列表数据加入新表格
# 添加标题
qhs_excle.range("A1:E1").value = ['姓名', '级别', '学历', '薪资', '地区']

flag = 1
for i in range_value_list:
    flag += 1
    # 获取行
    str_sheet1 = "A" + str(flag) + ":" + "E" + str(flag)
    qhs_excle.range(str_sheet1).value = i

# 保存数据
workbook.save("../source_material/02/华为奖励(1).xlsx")

# 关闭工作表
workbook.close()

# 关闭工作簿
app.quit()
