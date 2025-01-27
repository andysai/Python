# 导入模块
import xlwings as xw
import get_IP_Version_Kernel as tt


# 创建实例
app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open(r"D:\python\DSLR\获取服务器ip&内核版本\test.xlsx")

# 新增工作表
kernel_excle = workbook.sheets.add("内核版本统计")

# 添加标题
kernel_excle.range("A1:C1").value = ['IP', '操作系统', '内核']

for i in range(2, len(tt.TT)+1):
    # 添加行
    str_address_str = "A" + str(i)
    str_address_end = "D" + str(i)
    # 插入数据
    kernel_excle.range(str_address_str + ":" + str_address_end).value = tt.TT[i-2]

# 保存数据
workbook.save(r"D:\python\DSLR\获取服务器ip&内核版本\IP_version_kernel-20220623.xlsx")

# 关闭工作表
workbook.close()

# 关闭工作簿
app.quit()

