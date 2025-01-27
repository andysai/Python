# 导入模块
import xlwings as xw

# 原始数据处理
mess = []
with open('原数据.txt', 'r', encoding='utf-8') as f:
    mes = f.readlines()
    for i in mes:
        IP = i.strip().split("|")[0]
        agent = ' '
        reason = '操作系统版本过低，不支持'
        version = i.strip().split("|")[-1]
        remask = '操作系统版本过低，不支持'
        c = [IP, agent, reason, version, remask]
        mess.append(c)
        print(IP)
    f.close()

# # 创建实例
# app = xw.App(visible=True, add_book=False)
#
# # 打开工作簿
# workbook = app.books.open(r"D:\python\DSLR\统计rhel5版本数量\test.xlsx")
#
# # 新增工作表
# version_excle = workbook.sheets.add("RHEL5版本服务器统计")
#
# # 添加标题
# version_excle.range("A1:E1").value = ['服务器IP', '主机安全agent安装状态', '无法安装原因',	'操作系统版本', '备注']
#
# for i in range(2, len(mess)+1):
#     # 添加行
#     str_address_str = "A" + str(i)
#     str_address_end = "E" + str(i)
#     # 插入数据
#     version_excle.range(str_address_str + ":" + str_address_end).value = mess[i-2]
#
# # 保存数据
# workbook.save(r"D:\python\DSLR\统计rhel5版本数量\RHEL5版本服务器统计-20221215.xlsx")
#
# # 关闭工作表
# workbook.close()
#
# # 关闭工作簿
# app.quit()
#
