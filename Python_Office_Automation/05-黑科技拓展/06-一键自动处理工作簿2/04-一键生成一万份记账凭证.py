import xlwings as xw

# 1.读取信息
def read_sheet():
    list_value = []

    app = xw.App(visible=True, add_book=False)

    # 1.打开原工作簿
    workbook = app.books.open("../source_material/06/04一键生成一万份记账凭证/职员信息表.xlsx")

    # 2.获取信息
    sheet = workbook.sheets[0]
    rows = int(sheet.used_range.address.split("$")[-1])
    for i in range(2, rows + 1):
        num_value = "A" + str(i) + ":C" + str(i)
        if sheet.range(num_value).value[0] != None:
            list_value.append(sheet.range(num_value).value)

    # 3.保存工作簿
    save_close(app, workbook)
    return list_value

# 2.将获取列表的值写入新的工作簿
def set_workbook(list_info):
    for sheet_name in list_info:
        # 复制文件
        copy_file(sheet_name[0])
        # 写入数据
        app = xw.App(visible=False, add_book=False)
        workbook = app.books.open("../source_material/06/04一键生成一万份记账凭证/生成记账凭证/" + sheet_name[0] + ".xlsx")
        sheet = workbook.sheets[0]
        sheet.range("B4").value = "借款人：" + sheet_name[0]
        sheet.range("A3").value = sheet_name[2]
        list_range_value = list(str(int(sheet_name[1])))
        list_range_value.reverse()

        # 贷款方
        m = 1
        for i in list_range_value:
            dic_value = {1: "K", 2: "J", 3: "I", 4: "H", 5: "G", 6: "F", 7: "E", 8: "D"}
            range_value1 = dic_value[m] + str(7)
            range_value2 = dic_value[m] + str(16)
            m += 1
            sheet.range(range_value1).value = i
            sheet.range(range_value2).value = i

        # 借款方
        n = 1
        for i in list_range_value:
            dic_value = {1: "U", 2: "T", 3: "S", 4: "R", 5: "Q", 6: "P", 7: "O", 8: "N"}
            range_value1 = dic_value[n] + str(7)
            range_value2 = dic_value[n] + str(16)
            n += 1
            sheet.range(range_value1).value = i
            sheet.range(range_value2).value = i

        print("已生成：" + sheet_name[0] + "记账凭证")
        save_close(app, workbook)

# 根据姓名复制文件
def copy_file(file_name):
    file = open("../source_material/06/04一键生成一万份记账凭证/记账凭证模板.xlsx", "rb")
    data_file = file.read()
    file.close()

    # 写入文件
    f = open("../source_material/06/04一键生成一万份记账凭证/生成记账凭证/" + file_name + ".xlsx", "wb")
    f.write(data_file)
    f.close()

# 4.保存和退出程序
def save_close(app, workbook):
    workbook.save()
    workbook.close()
    app.quit()
    # app.kill()

# python程序执行入口
if __name__ == "__main__":
    # 1.读取表格信息
    list_info = read_sheet()

    # 2.将获取列表的值写入新的工作簿
    set_workbook(list_info)
