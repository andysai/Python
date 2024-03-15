# 导入模块
import datetime
import xlwings as xw
import os

# 获取当前时间
curret_date = datetime.datetime.now()
year = curret_date.year
month = curret_date.month
day = curret_date.day
excle_time = str(year) + "-" + str(month) + "-" + str(day)

# 创建实例
app = xw.App(visible=True, add_book=False)

# 判断文件是否存在，存在则打开，不存在则创建
if not os.path.exists("设备在架情况变更表.xlsx"):
    # 新建工作簿
    workbook = app.books.add()
else:
    # 打开工作簿
    workbook = app.books.open("设备在架情况变更表.xlsx")

# 判断子表是否存在，存在则继续添加数据，不存在则创建并添加数据
# 获取所有的子表
sheets = workbook.sheets
sheet_list =[]
for i in sheets:
    sheet_list.append(i.name)

if '变更表' not in sheet_list:
    sheet = workbook.sheets.add('变更表')
    sheet.activate()

else:
    sheet = workbook.sheets['变更表']
    sheet.activate()

def sheet_Style():
    # 第一行表格属性设置
    fg1 = sheet.range("A1:F1")
    fg1.api.Merge()
    fg1.value = "云达信设备在架情况变更表"
    fg1.color = (53, 203, 78)
    fg1.api.HorizontalAlignment = -4108
    fg1.api.VerticalAlignment = -4108
    fg1.column_width = 15
    fg1.row_height = 48
    fg1.api.Font.Name = "宋体"
    fg1.api.Font.Size = 26
    fg1.api.Font.Bold = True
    fg1.api.Borders(7).LineStyle = 1
    fg1.api.Borders(7).Weight = 2
    fg1.api.Borders(8).LineStyle = 1
    fg1.api.Borders(8).Weight = 2
    fg1.api.Borders(9).LineStyle = 1
    fg1.api.Borders(9).Weight = 2
    fg1.api.Borders(10).LineStyle = 1
    fg1.api.Borders(10).Weight = 2
    fg1.api.Borders(11).LineStyle = 1
    fg1.api.Borders(11).Weight = 2
    fg1.api.Borders(12).LineStyle = 1
    fg1.api.Borders(12).Weight = 2

    # 第二行表格属性设置
    fg2 = sheet.range("A2:F2")
    fg2.value = ['位置', '变更内容', '变更原因', '变更时间', '修改人', '备注']
    fg2.api.HorizontalAlignment = -4108
    fg2.api.VerticalAlignment = -4108
    fg2.column_width = 18
    fg2.row_height = 33
    fg2.api.Font.Name = "宋体"
    fg2.api.Font.Size = 15
    fg2.api.Font.Bold = False
    fg2.api.Borders(7).LineStyle = 1
    fg2.api.Borders(7).Weight = 2
    fg2.api.Borders(8).LineStyle = 1
    fg2.api.Borders(8).Weight = 2
    fg2.api.Borders(9).LineStyle = 1
    fg2.api.Borders(9).Weight = 2
    fg2.api.Borders(10).LineStyle = 1
    fg2.api.Borders(10).Weight = 2
    fg2.api.Borders(11).LineStyle = 1
    fg2.api.Borders(11).Weight = 2
    fg2.api.Borders(12).LineStyle = 1
    fg2.api.Borders(12).Weight = 2

    # 第三行表格属性设置
    fg3 = sheet.range("A3:F3")
    fg3.value = ['例：F2-M2-G16', '下架2台DELL R720服务器', '下架', '', '冼永康', '无']
    fg3.api.HorizontalAlignment = -4108
    fg3.api.VerticalAlignment = -4108
    fg3.column_width = 18
    fg3.row_height = 25
    fg3.api.Font.Name = "宋体"
    fg3.api.Font.Size = 10
    fg3.api.Font.Bold = False
    fg3.api.Borders(7).LineStyle = 1
    fg3.api.Borders(7).Weight = 2
    fg3.api.Borders(8).LineStyle = 1
    fg3.api.Borders(8).Weight = 2
    fg3.api.Borders(9).LineStyle = 1
    fg3.api.Borders(9).Weight = 2
    fg3.api.Borders(10).LineStyle = 1
    fg3.api.Borders(10).Weight = 2
    fg3.api.Borders(11).LineStyle = 1
    fg3.api.Borders(11).Weight = 2
    fg3.api.Borders(12).LineStyle = 1
    fg3.api.Borders(12).Weight = 2

    # 内容表格属性设置
    fg4 = sheet.range("A4:F160")
    fg4.api.HorizontalAlignment = -4108
    fg4.api.VerticalAlignment = -4108
    fg4.column_width = 18
    fg4.row_height = 25
    fg4.api.Font.Name = "宋体"
    fg4.api.Font.Size = 10
    fg4.api.Font.Bold = False
    fg4.api.Borders(7).LineStyle = 1
    fg4.api.Borders(7).Weight = 2
    fg4.api.Borders(8).LineStyle = 1
    fg4.api.Borders(8).Weight = 2
    fg4.api.Borders(9).LineStyle = 1
    fg4.api.Borders(9).Weight = 2
    fg4.api.Borders(10).LineStyle = 1
    fg4.api.Borders(10).Weight = 2
    fg4.api.Borders(11).LineStyle = 1
    fg4.api.Borders(11).Weight = 2
    fg4.api.Borders(12).LineStyle = 1
    fg4.api.Borders(12).Weight = 2

sheet_Style()

# 定义写入数据函数
def input_data(str_value_list):
    for i in range(4, 1601):
        str_address = "A" + str(i)
        str_address_he = "F" + str(i)
        if sheet.range(str_address).value == None:
            # 写入数据
            sheet.range(str_address).value = str_value_list
            # 居中
            sheet.range(str_address + ":" + str_address_he).api.HorizontalAlignment = -4108
            sheet.range(str_address + ":" + str_address_he).api.VerticalAlignment = -4108
            break
        else:
            continue

# 主体循环
flag = True
while flag:
    set_run = input("请按要求输入1.添加数据 2.结束(1 or 2):")
    if set_run == "1":
        location = input("请输入设备位置:")
        change_content = input("请输入变更内容:")
        change_reason = input("请输入变更原因:")
        modified_by = input("请输入修改人姓名:")
        remarks = input("请输入备注内容:")

        # 定义格式输出
        str_value_list = [location, change_content, change_reason, excle_time, modified_by, remarks]
        input_data(str_value_list)

    elif set_run == "2":
        # 保存
        workbook.save("设备在架情况变更表.xlsx")
        # 关闭工作表
        workbook.close()
        # 关闭工作簿
        app.quit()
        flag = False

    else:
        print("请按照要求输入你的选择!")
