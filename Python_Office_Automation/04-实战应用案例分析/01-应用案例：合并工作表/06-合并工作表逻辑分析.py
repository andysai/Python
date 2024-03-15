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
            list_address.append(int(address_all))

    return list_address

# 3 根据位置，将数值放进合并的表格中
def set_merge_sheet(workbook, list_address):
    # 先写第一行数据
    workbook.sheets["合并工作表"].range("A1:E1").value = workbook.sheets[1].range("A1:E1").value
    # 循环写入数值
    for address in list_address:
        # 获得每一个表格对象
        sht = workbook.sheets[list_address.index(address)+1]



    # 添加人力资源部的数据

    # 添加生产技术部的数据
    # 添加计划营销部的数据
    # 添加安全监督部的数据
    # 添加财务部的数据
    # 添加后勤部的数据
    # 添加保卫部的数据
    # 添加生产技术部的数据

# 4 python程序执行入口
if __name__ == "__main__":
    # 1 新增工作表
    obj_workbook = add_sheet()
    # 2 获取每个表中的最后的位置信息
    list_address = get_sheet_value(obj_workbook)
    # 3 根据位置，将数值放进合并的表格中
    set_merge_sheet(obj_workbook, list_address)



