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

# 定义写入数据函数
# def input_data(str_value_list):
#     pass

# 创建循环主体
# flag = True
# while True:
#     # 循环获取用户输入
#     print("请如下格式输入售卖信息:")
#     print("苹果 2.5 45")
#     str_value = input("请输入:")
#     str_value_list = str_value.split(" ")
#
#     if str_value == '保存':
#         # 保存工作簿
#         workbook.save("../source_material/销售记录单(1).xlsx")
#         # 关闭工作簿
#         workbook.close()
#         # 退出工作簿
#         app.quit()
#         flag = False
#     else:
#         str_value_list = str_value.split(" ")
#         input_data(str_value_list)
