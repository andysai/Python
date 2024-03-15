import xlwings as xw

#1.新增工作表
def add_sheet():
    app=xw.App(visible=True,add_book=False)
    #1.打开原工作簿
    workbook = app.books.open("合并工作表.xlsx")
    #2.新增表格
    workbook.sheets.add("合并工作表")

    return workbook
    
'''
合并的使用要注意，你的工作簿文件名必须要和这个-合并工作表.xlsx保持一致。
'''
   
#2.获取每个表中的最后位置信息
def get_sheet_value(workbook):
    listsht = workbook.sheets #获取所有工作表
    list_address = []   #创建一个空列表，放置每个表的最后位置信息

    for sheet in listsht:
        if sheet.name != "合并工作表":
            address_all = sheet.used_range.address.split("$")[-1]
            list_address.append(int(address_all))
            
    return list_address

#3.根据位置，将数值放进合并的表格中
def set_merge_sheet(workbook,list_address):
    #先写第一行数据
    e = workbook.sheets[1].used_range.address.split("$")[-2]
    str_address_one = "A1:"+e+"1"
    workbook.sheets["合并工作表"].range(str_address_one).value = workbook.sheets[1].range(str_address_one).value
    
    #循环写入数值
    for address_one in list_address:
        #获得每一个表格对象
        sht = workbook.sheets[list_address.index(address_one)+1]

        str_address = "A2:"+e+str(address_one)  
        #获得每一个表格的值
        sht_value = sht.range(str_address).value

        #创建合并的表格对象
        sheet_merge = workbook.sheets["合并工作表"]

        #将这个值放到合并工作表中
        if list_address.index(address_one) == 0:
            sheet_merge.range(str_address).value = sht_value
        else:
            #获取合并单元格当前的有效区域
            str_name = sheet_merge.used_range.address.split("$")[-1]
            a_address = "A"+str(int(str_name)+1)+":"
            b_address = "E"+ str(int(str_name)+1+address_one)
            sheet_merge.range(a_address+b_address).value = sht_value

#4.保存和退出程序
def sava_close(workbook):
    workbook.save()
    workbook.close()
    


#python程序执行入口
if __name__ == "__main__":

    #1.新增工作表,返回workbook对象
    obj_workbook = add_sheet()

    #2.获取每个表最后的位置信息
    list_address =get_sheet_value(obj_workbook)

    #3.根据位置，将数值放进合并的表格中
    set_merge_sheet(obj_workbook,list_address)

    #4.保存和退出程序
    #sava_close(obj_workbook)

    

    
    
