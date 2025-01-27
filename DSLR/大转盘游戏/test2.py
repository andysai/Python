import json
import re
import openpyxl

list = []
with open('广东数据.txt', 'r', encoding='utf-8') as project:
    gd_messages = project.readlines()

    for gd_message in gd_messages:
        list.append(gd_message)

wb = openpyxl.Workbook()
ws = wb.active
for i in list:
    print(len(i))
    print(i)

# wb.save('test.xlsx')
# wb.close()
