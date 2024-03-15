import openpyxl

wb = openpyxl.load_workbook('新机房统计表-20191213.xlsx')
sheet = wb['机架服务器设备总表']
data = []
for i in sheet:
    data_1 = []
    for cell in i:
        data_1.append(cell.value)
    data.append(data_1)
#print(data)
lists = []
for i in data:

    if (i[9] == 'R720') or (i[9] == 'X3950M2') or (i[9] == 'R910'):
        if i[12] == '物理':
            if (i[49] == '空闲') or (i[49] == '关机'):
                if (i[15] == '广电院') or (i[15] == '育成中心') or (i[15] ==  '云达信') or (i[15] == '调拨'):
                    name = str(i[8]) + '-' + str(i[9])
                    if i[19] == None:
                        i[19] = '16C'
                        CPU = i[19]
                    else:
                        CPU = i[19]
                    if CPU == '2*6C*2':
                        CPU = '24C'
                    elif CPU == '2*10C*2':
                        CPU = 'DELL　Ｒ720　40C.txt'
                    elif CPU == '4*4C':
                        CPU = '16C'
                    elif CPU == '4*8C*2':
                        CPU = '64C'
                    if i[20] == None and i[9] != 'R720':
                        i[20] = '128G'
                        Memory = i[20]
                    else:
                        Memory = i[20]
                    if Memory == '128G(16*8G)':
                        Memory = '128G'
                    elif Memory == '48G(6*8G)':
                        Memory = '48G'
                    elif Memory == '32G(4*8G)':
                        Memory = '32G'
                    elif Memory == '64G(4*16G)':
                        Memory = '64G'
                    elif Memory == '128G(8*16G)':
                        Memory = '128G'
                    elif Memory == '256G(16*16G)':
                        Memory = '256G'
                    elif Memory =='64G(8*8G)':
                        Memory = '64G'
                    elif Memory == '128G(32*4G)':
                        Memory = '128G'
                    elif Memory == '64G(16*4G)':
                        Memory = '64G'
                    message = [name,CPU,Memory]
                    lists.append(message)
# print(lists)
IBM = []
DELL_24_32 = []
DELL_24_48 = []
DELL_24_64 = []
DELL_24_128 = []
DELL_40_64 = []
DELL_40_128 = []
DELL_40_256 = []
DELL_64_64 = []
DELL_64_128 = []

for list in lists:
    # if list[0] == 'DELL-R910':
    #     print(list[1],list[2])
    if list[0] == 'IBM-X3950M2':
        IBM.append(list[0])
    # 24C CPU ,内存有32G，48G，64G，128G
    elif list[0] == 'DELL-R720' and list[1] == '24C' and list[2] == '32G':
        DELL_24_32.append(list[0])
    elif list[0] == 'DELL-R720' and list[1] == '24C' and list[2] == '48G':
        DELL_24_48.append(list[0])
    elif list[0] == 'DELL-R720' and list[1] == '24C' and list[2] == '64G':
        DELL_24_64.append(list[0])
    elif list[0] == 'DELL-R720' and list[1] == '24C' and list[2] == '128G':
        DELL_24_128.append(list[0])
    # 40CCPU ,内存有64G，128G，256G
    elif list[0] == 'DELL-R720' and list[1] == 'DELL　Ｒ720　40C.txt' and list[2] == '64G':
        DELL_40_64.append(list[0])
    elif list[0] == 'DELL-R720' and list[1] == 'DELL　Ｒ720　40C.txt' and list[2] == '64G':
        DELL_40_128.append(list[0])
    elif list[0] == 'DELL-R720' and list[1] == 'DELL　Ｒ720　40C.txt' and list[2] == '64G':
        DELL_40_256.append(list[0])
    elif list[0] == 'DELL-R910' and list[1] == '64C' and list[2] == '64G':
        DELL_64_64.append(list[0])
    elif list[0] == 'DELL-R910' and list[1] == '64C' and list[2] == '128G':
        DELL_64_128.append(list[0])




print(len(DELL_64_128))
reward_ws = wb.create_sheet(title='空闲服务器资源统计')
sheet['A1'] = '设备型号'
sheet['B1'] = 'CPU'
sheet['C1'] = '内存'
sheet['D1'] = '数量'
list_all = []



wb.save('1.xlsx')