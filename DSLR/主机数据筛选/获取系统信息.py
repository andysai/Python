# 导入模块
import xlwings as xw

# 创建实例
app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open("D:\study\DSLR\主机数据筛选\IP_passwd.xlsx")

# 筛选并添加数据
# 1.1 获取所有表格数据
sheets_list = workbook.sheets

# 1.2 将筛选的数据存入列表
# 创建一个空列表，用于存放数据
range_value_list = []
def readrange(excle):
    for i in range(1, 1394):
        # 组合字符
        # 获取单个单元格
        str_sheet_B = "B" + str(i)
        str_sheet_D = "D" + str(i)
        # 获取行
        str_sheet1 = "A" + str(i) + ":" + "D" + str(i)
        # 获取B列的值
        str_value_B = excle.range(str_sheet_B).value
        # 获取D列的值
        str_value_D = excle.range(str_sheet_D).value
        # 判断是否是root和ssh协议
        if str_value_D == " SSH:22" and str_value_B == ' root':
            str_sheet_row = excle.range(str_sheet1).value
            range_value_list.append(str_sheet_row)

# 获取每个表格的名称
for excle in sheets_list:
    readrange(excle)

# 讲txt的数据存入到列表
ip_addresses = []
with open('system.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        ip_addresses.append(i.strip())

# 获取操作系统和IP信息
ip_lists = []
for ip_list in ip_addresses:
    system_name = ip_list.split("-")[1]
    IP_address = ip_list.split("-")[-1]
    server_mes = system_name + '-' + IP_address
    ip_lists.append(server_mes)

# 去掉windows机器，并讲所有的linux版本筛选出来
system_news = []
for i in ip_lists:
    if i[:1] != 'w':
        system_news.append(i)

# 去掉已经在ansible上添加过的主机
ansible_host = []
with open('absible_host.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        ansible_host.append(i.strip())

no_IP = []
for i in system_news:
    if i.split('-')[-1] not in ansible_host:
        no_IP.append(i.split('-')[-1])

for i in range_value_list:
    if i[0].strip() in no_IP :
        print('ssh-copy-id -i ~/.ssh/id_rsa.pub ' + i[1].strip() + "@" + i[0].strip() + ' ' + i[2].strip())


# 新增工作表
qhs_excle = workbook.sheets.add("ssh")

# 1.3 列表数据加入新表格
# 添加标题
qhs_excle.range("A1:D1").value = ['IP', '账号', '密码', '协议']

flag = 1
for i in range_value_list:
    flag += 1
    # 获取行
    str_sheet1 = "A" + str(flag) + ":" + "D" + str(flag)
    qhs_excle.range(str_sheet1).value = i

# 保存数据
workbook.save("D:\study\DSLR\主机数据筛选\IP_passwd_1.xlsx")

# 关闭工作表
workbook.close()

# 关闭工作簿
app.quit()

