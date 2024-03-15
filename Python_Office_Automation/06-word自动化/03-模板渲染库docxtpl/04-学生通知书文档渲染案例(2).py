# 导入模块
from docxtpl import DocxTemplate
import xlwings as xw

# 读取excle数据
def read_sheet():
    # 创建空列表
    list_value = []
    # 创建实例
    app = xw.App(visible=True, add_book=False)
    # 打开工作簿
    workbook = app.books.open("../source_material/03/A/学生信息表.xlsx")
    # 打开工作表
    sheets = workbook.sheets[0]
    # 封装列表
    sheet_list = sheets.used_range.value
    # 统计工作表行数
    sheet_row_num = len(sheet_list)
    # 统计工作表列数
    sheet_col_num = len(sheet_list[0])
    # 遍历工作表数据
    for i in range(1, sheet_row_num):
        # 创建空字典
        sheet_dict = {}
        for j in range(0, sheet_col_num):
            if type(sheet_list[i][j]) == float:
                sheet_dict[sheet_list[0][j]] = str(sheet_list[i][j])[:-2]
            else:
                sheet_dict[sheet_list[0][j]] = sheet_list[i][j]

        list_value.append(sheet_dict)

    # 保存退出
    save_close(app, workbook)
    return list_value

# 保存退出
def save_close(app, workbook):
    workbook.close()
    app.quit()

# 数据写入
def write_data(list_value):
    for list_dict in list_value:
        # 加载模板文件
        document = DocxTemplate("../source_material/03/A/学生通知书_模板.docx")
        document.render(list_dict)
        document.save("../source_material/03/A/学生通知书/" + list_dict["姓名"].strip() + ".docx")
        print(list_dict["姓名"].strip() + "的材料正在保存中...")

# 程序执行入口
if __name__ == '__main__':
    # 读取数据
    sheet_list_value = read_sheet()
    # 写入数据
    write_data(sheet_list_value)
