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
        sheet_dic = {}
        # 如何构建字典
        for j in range(0, len(sheet_list[0])):
            if type(sheet_list[i][j]) == float:
                sheet_dic[sheet_list[0][j]] = str(sheet_list[i][j])[:-2]
            else:
                sheet_dic[sheet_list[0][j]] = sheet_list[i][j]

        list_value.append(sheet_dic)

    # 保存退出
    save_close(app, workbook)
    return list_value
# 保存退出
def save_close(app, workbook):
    workbook.close()
    app.quit()

# 程序执行入口
if __name__ == "__main__":
    # 读取工作表的数据
    sheet_list_value = read_sheet()
