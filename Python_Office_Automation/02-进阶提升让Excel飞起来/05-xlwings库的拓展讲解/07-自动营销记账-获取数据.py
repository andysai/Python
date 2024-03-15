# 导入模块
import xlwings as xw



flag = True
while True:
    # 循环获取用户输入
    print("请如下格式输入售卖信息:")
    print("苹果 2.5 45")
    str_value = input("请输入:")
    str_value_list = str_value.split(" ")

    if str_value == '保存':
        # 保存工作簿
        workbook.save("../source_material/销售记录单(1).xlsx")
        # 关闭工作簿
        workbook.close()
        # 退出工作簿
        app.quit()
        flag = False
    else:
        str_value_list = str_value.split(" ")
        input_data(str_value_list)
