# 导入模块
import xlwings as xw
import datetime

# 日期格式编写
month = str(datetime.datetime.now().month)
day = str(datetime.datetime.now().day)
time_str = month + "月" + day + "日"

# 创建实例
app = xw.App(visible=True, add_book=False)
# 打开工作簿
workbook = app.books.add()
# 打开工作表
worksheet = workbook.sheets.add(time_str)

# 定义风格样式
def sheet_Style():
    # 合并第一行单元格
    fg1 = worksheet.range("A1:D1")
    fg1.api.Merge()
    fg1.value = "***超市营销记录"
    fg1.api.Font.Size = 25
    fg1.api.HorizontalAlignment = -4108
    fg1.api.VerticalAlignment = -4108

    # 设置第二行单元格
    fg2 = worksheet.range("A2:D2")
    fg2.value = ["类目", "单价", "数量", "总价"]
    fg2.api.Font.Bold = True
    fg2.api.HorizontalAlignment = -4108
    fg2.api.VerticalAlignment = -4108

    # 设置边界线
    fg3 = worksheet.range("A2:D100")
    # 内部边框垂直
    fg3.api.Borders(11).LineStyle = 1
    fg3.api.Borders(11).Weight = 2
    # 内部边框水平
    fg3.api.Borders(12).LineStyle = 1
    fg3.api.Borders(12).Weight = 2


sheet_Style()

# 定义写入数据函数
def input_data(str_value_list):
    print("-----------------")
    for i in range(3, 101):
        str_address = "A" + str(i)
        str_address_he = "D" + str(i)
        if worksheet.range(str_address).value == None:
            # 写入数据
            worksheet.range(str_address).value = str_value_list
            worksheet.range(str_address_he).value = float(str_value_list[1]) * int(str_value_list[2])
            # 居中
            worksheet.range(str_address + ":" + str_address_he).api.HorizontalAlignment = -4108
            worksheet.range(str_address + ":" + str_address_he).api.VerticalAlignment = -4108
            break
        else:
            continue
# 创建循环主体
flag = True
while flag:
    # 循环获取用户输入
    print("请如下格式输入售卖信息:")
    print("苹果 2.5 45")
    str_value = input("请输入:")

    if str_value == '保存':
        # 保存工作簿
        workbook.save("销售记录单.xlsx")
        # 关闭工作簿
        workbook.close()
        # 退出工作簿
        app.quit()
        flag = False
    else:
        str_value_list = str_value.split(" ")
        input_data(str_value_list)
