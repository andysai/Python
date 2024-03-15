# 导入模块
import xlwings as xw

# 1 新增工作表
def add_sheet():
    app = xw.App(visible=True,add_book=False)
    # 2 打开原工作簿
    workbook = app.books.open("../source_material/01/合并工作表.xlsx")
    # 3 新增工作表
    workbook.sheets.add("合并工作表")

# python程序执行入口
if __name__ == "__main__":
    # 1 新增工作表
    add_sheet()
