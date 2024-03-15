import xlwt

newbook = xlwt.Workbook()

worksheet = newbook.add_sheet("测试")

strs = ["我", "是", "谁", "哦", "啊"]

for i in range(len(strs)):
    worksheet.write(0, i, strs[i])
    print(0, i, strs[i])
newbook.save("source_material/01-來大仙.xls")
print("执行完成")
