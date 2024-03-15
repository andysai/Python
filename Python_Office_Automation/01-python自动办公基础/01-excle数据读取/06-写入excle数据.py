# 导入模块
import xlwt

# 创建新的工作簿
newwb = xlwt.Workbook()

# 创建新的工作表
worksheet = newwb.add_sheet("A组薪资表")

# 写入数据
# worksheet.write(0,0,"职工号")
# worksheet.write(0,1,"姓名")
# worksheet.write(1,0,"aa")

strs = ['职工号','姓名','性别','年龄','所属部门','职工类型','基本工资','事假天数']

for i in range(len(strs)):
     worksheet.write(0,i,strs[i])

# 保存数据
newwb.save("../source_material/2019年某公司新资表.xls")