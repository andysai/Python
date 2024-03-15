# 导入模块
import xlwings as xw

# 1 新增工作表
def add_sheet():
    app = xw.App(visible=True,add_book=False)
    # 2 打开原工作簿
    workbook = app.books.open("../source_material/01/合并工作表.xlsx")
    # 3 新增工作表
    workbook.sheets.add("合并工作表")

    return workbook

# 2 获取每个表中的最后的位置信息
def get_sheet_value(workbook):
    # 获取所有工作表
    listsht = workbook.sheets
    # 创建一个空列表，放置每个表的最后位置信息
    list_address = []
    for sheet in listsht:
        if sheet.name != "合并工作表":
            address_all = sheet.used_range.address.split("$")[-1]
            list_address.append(address_all)

    return list_address

# python程序执行入口
if __name__ == "__main__":
    # 1 新增工作表
    obj_workbook = add_sheet()
    # 2 获取每个表中的最后的位置信息
    list_address = get_sheet_value(obj_workbook)
    for i in list_address:
        print(i)