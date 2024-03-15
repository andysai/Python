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

# python程序执行入口
if __name__ == "__main__":
    # 1 新增工作表
    obj_workbook = add_sheet()
    # 2 获取每个表中的最后的位置信息
    get_sheet_value(obj_workbook)