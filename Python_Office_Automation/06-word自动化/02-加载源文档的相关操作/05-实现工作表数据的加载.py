# 导入库
import xlwings as xw
from docx import Document
from docx2python import docx2python


# 读取工作表的数据
def read_sheet():
    list_value = []
    app = xw.App(visible=True, add_book=False)
    # 打开工作簿
    workbook = app.books.open("../source_material/02/A/学生信息表.xlsx")
    # 获取信息表
    sheet = workbook.sheets[0]
    # 封装列表
    sheet_list = sheet.used_range.value
    for i in range(1, len(sheet_list)):
        # 创建空字典
        sheet_dict = {}
        # 如何构建字典

        list_value.append(sheet_dict)
    return list_value


# 程序执行入口
if __name__ == "__main__":
    # 读取工作表的数据
    read_sheet()
