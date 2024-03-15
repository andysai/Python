import xlwings as xw

# 创建实例
app = xw.App(visible=True, add_book=False)
# 优先使用相对路径打开工作簿
workbook = app.books.open('./新机房设备统计表-20210326.xlsx', password='idc123!@#')

# 获取表格数据
sheets = workbook.sheets[0]

# 获取总行数
nrows = sheets.used_range.last_cell.row

# 获取列表的所有数据
sheets_row_list = []
for i in range(4, nrows+1):
    first = "$A" + str(i) + ":" + "$AY" + str(i)
    sheets_row_list.append(sheets.range(first).value)

# 添加表头
expire_list = []
head = ['设备位置', '设备型号', '设备类别', '内部地址', '客户名称', '客户接口人', '到期时间', '状态']
expire_list.append(head)

# 获取表头相关数据
valid_datas = []
for valid_data in sheets_row_list:
    mes = [valid_data[3], valid_data[4], valid_data[5], valid_data[7], valid_data[8], valid_data[9], valid_data[12], valid_data[30], valid_data[37], valid_data[38], valid_data[48], valid_data[49]]
    valid_datas.append(mes)

# 获取设备有效数据
# Equipment_locations = []
# for new_valid_data in valid_datas:
#     # print(new_valid_data)
#     if (new_valid_data[0] == 'CascIdc' and new_valid_data[2] is not None and new_valid_data[2] != 'Warehouse') and (new_valid_data[4] is None and new_valid_data[5] is not None):
#         Equipment_location = new_valid_data[0] + '-' + new_valid_data[1] + '-' + str(new_valid_data[2]) + '-' + new_valid_data[3] + '-' + new_valid_data[5] + '-' + new_valid_data[6] + '-' + new_valid_data[7] + '-' + new_valid_data[8] + '-' + new_valid_data[9] + '-' + new_valid_data[10] + '-' + new_valid_data[11] + '-' + new_valid_data[12]
#         Equipment_locations.append(Equipment_location)
#     elif (new_valid_data[0] == 'CascIdc' and new_valid_data[2] is not None and new_valid_data[2] != 'Warehouse') and (new_valid_data[4] is not None and new_valid_data[5] is None):
#         Equipment_location = new_valid_data[0] + '-' + new_valid_data[1] + '-' + str(new_valid_data[2]) + '-' + new_valid_data[3] + '-' + new_valid_data[4] + '-' + new_valid_data[6] + '-' + new_valid_data[7] + '-' + new_valid_data[8] + '-' + new_valid_data[9] + '-' + new_valid_data[10] + '-' + new_valid_data[11] + '-' + new_valid_data[12]
#         Equipment_locations.append(Equipment_location)
#     elif (new_valid_data[0] == 'CascIdc' and new_valid_data[2] is not None and new_valid_data[2] != 'Warehouse') and (new_valid_data[4] is not None and new_valid_data[5] is not None):
#         Equipment_location = new_valid_data[0] + '-' + new_valid_data[1] + '-' + str(new_valid_data[2]) + '-' + new_valid_data[3] + '-' + new_valid_data[4] + '-' + new_valid_data[5] + '-' + new_valid_data[6] + '-' + new_valid_data[7] + '-' + new_valid_data[8] + '-' + new_valid_data[9] + '-' + new_valid_data[10] + '-' + new_valid_data[11] + '-' + new_valid_data[12]
#         Equipment_locations.append(Equipment_location)
#
# print(Equipment_locations)
# for new_valid_data in valid_datas:
#     print(new_valid_data[7])
a = ''
b = 1
if a is None or b is None:
    print(a or b)