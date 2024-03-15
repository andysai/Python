import xlwings as xw
import datetime
import time

date = datetime.date.today()
time = time.strftime("%H:%M")

# 创建实例
app = xw.App(visible=True, add_book=False)

# 新建工作簿
workbook = app.books.add()

# 打开工作表
worksheet = workbook.sheets.add("事件流程")

#  定义表头的风格样式
def head_sheet_style():
    fg1 = worksheet.range("A1:G1")
    fg1.api.Merge()
    fg1.value = "事件服务单"
    fg1.api.Font.Size = 25
    fg1.api.Font.Name = "华文隶书"
    fg1.api.HorizontalAlignment = -4108
    fg1.api.VerticalAlignment = -4108
    fg1.api.Borders(8).LineStyle = 1
    fg1.api.Borders(8).Weight = 3
    fg1.api.Borders(9).LineStyle = 1
    fg1.api.Borders(9).Weight = 3
    fg1.api.Borders(7).LineStyle = 1
    fg1.api.Borders(7).Weight = 3
    fg1.api.Borders(10).LineStyle = 1
    fg1.api.Borders(10).Weight = 3

# 定义小标题的风格样式
def first_sheet_style():
    fg2 = worksheet.range("A4:G4, A8:G8, A13:G13")
    fg2.api.Merge()
    for i in range(3):
        if i == 0:
            worksheet.range("A4").value = "客户信息"
        elif i == 1:
            worksheet.range("A8").value = "基本信息"
        elif i == 2:
            worksheet.range("A13").value = "处理信息"

    fg2.color = (255, 205, 155)
    fg2.api.Font.Size = 12
    fg2.api.Font.Name = "宋体"
    fg2.api.Font.Bold = True
    fg2.api.RowHeight = 22
    fg2.api.VerticalAlignment = -4108
    fg2.api.Borders(8).LineStyle = 1
    fg2.api.Borders(8).Weight = 3
    fg2.api.Borders(9).LineStyle = 1
    fg2.api.Borders(9).Weight = 3
    fg2.api.Borders(7).LineStyle = 1
    fg2.api.Borders(7).Weight = 3
    fg2.api.Borders(10).LineStyle = 1
    fg2.api.Borders(10).Weight = 3

    fg3 = worksheet.range("A18:G18")
    fg3.api.Merge()
    fg3.value = "用户确认:"
    fg3.color = (255, 205, 155)
    fg3.api.Font.Size = 12
    fg3.api.Font.Name = "宋体"
    fg3.api.Font.Bold = True
    fg3.api.RowHeight = 37.25
    fg3.api.VerticalAlignment = -4108
    fg3.api.Borders(8).LineStyle = 1
    fg3.api.Borders(8).Weight = 3
    fg3.api.Borders(9).LineStyle = 1
    fg3.api.Borders(9).Weight = 3
    fg3.api.Borders(7).LineStyle = 1
    fg3.api.Borders(7).Weight = 3
    fg3.api.Borders(10).LineStyle = 1
    fg3.api.Borders(10).Weight = 3

# 定义内容的风格样式
def second_sheet_style():
    fg4 = worksheet.range("A2, G2, A3, G3, A5, F5, A6, F6, A7, F7, A9, F9, A11, A12, A16, F16, A17, F17")
    for i in range(18):
        if i == 0:
            worksheet.range("A2").value = "事件单号"
        elif i == 1:
            worksheet.range("G2").value = "登记日期:" + str(date)
            worksheet.range("G2").autofit()
        elif i == 2:
            worksheet.range("A3").value = "登记人"
        elif i == 3:
            worksheet.range("G3").value = "登记时间:" + time
        elif i == 4:
            worksheet.range("A5").value = "客户名称"
        elif i == 5:
            worksheet.range("F5").value = "用户地址"
        elif i == 6:
            worksheet.range("A6").value = "联系人"
        elif i == 7:
            worksheet.range("F6").value = "联系电话"
        elif i == 8:
            worksheet.range("A7").value = "服务单位"
        elif i == 9:
            worksheet.range("F7").value = "电子邮件"
        elif i == 10:
            worksheet.range("A9").value = "事件类别"
        elif i == 11:
            worksheet.range("F9").value = "服务级别"
        elif i == 12:
            worksheet.range("A11").value = "事件级别"
        elif i == 13:
            worksheet.range("A12").value = "事件状态"
        elif i == 14:
            worksheet.range("A16").value = "响应事件"
        elif i == 15:
            worksheet.range("F16").value = "到场时间"
        elif i == 16:
            worksheet.range("A17").value = "解决时间"
        elif i == 17:
            worksheet.range("F17").value = "执行人"

    fg4.color = (192, 192, 192)
    fg4.api.Font.Size = 10
    fg4.api.Font.Name = "宋体"
    fg4.api.RowHeight = 17.25
    fg4.api.HorizontalAlignment = -4108
    fg4.api.VerticalAlignment = -4108
    fg4.api.Borders(8).LineStyle = 1
    fg4.api.Borders(8).Weight = 3
    fg4.api.Borders(9).LineStyle = 1
    fg4.api.Borders(9).Weight = 3
    fg4.api.Borders(7).LineStyle = 1
    fg4.api.Borders(7).Weight = 3
    fg4.api.Borders(10).LineStyle = 1
    fg4.api.Borders(10).Weight = 3

    fg6 = worksheet.range("A19:B19")
    fg6.api.Merge()
    fg6.value = "是否建议提交问题管理"
    fg6.color = (192, 192, 192)
    fg6.api.Font.Size = 10
    fg6.api.Font.Name = "宋体"
    fg6.api.RowHeight = 17.25
    fg6.api.HorizontalAlignment = -4108
    fg6.api.VerticalAlignment = -4108
    fg6.api.Borders(8).LineStyle = 1
    fg6.api.Borders(8).Weight = 3
    fg6.api.Borders(9).LineStyle = 1
    fg6.api.Borders(9).Weight = 3
    fg6.api.Borders(7).LineStyle = 1
    fg6.api.Borders(7).Weight = 3
    fg6.api.Borders(10).LineStyle = 1
    fg6.api.Borders(10).Weight = 3

def hebing_sheet_style():
    fg5 = worksheet.range("B2:F2, B3:F3, B5:E5, B6:E6, B7:E7, B9:E9, B11:G11, B12:G12, B16:E16, B17:E17, C19:D19")
    fg5.api.Merge()
    for i in range(4):
        if i == 0:
            worksheet.range("B9").value = "○ 网络服务 ○ 灾备服务 ○ 运维服务 ○ 技术咨询 ○ 备案服务 ○ 其他"
            worksheet.range("B9:E9").column_width = 14
        elif i == 1:
            worksheet.range("B11").value = "  ○ 高               ○ 中                ○ 低  "
        elif i == 2:
            worksheet.range("B12").value = "○ 已登记  ○ 一线处理中  ○ 二线处理中  ○ 等待指出处理中  ○ 三线处理中  ○ 已确认  ○ 已关闭"
        elif i == 3:
            worksheet.range("C19").value = "○提交   ○不提交"

    fg5.api.Font.Size = 10
    fg5.api.Font.Name = "宋体"
    fg5.api.HorizontalAlignment = -4108
    fg5.api.VerticalAlignment = -4108
    fg5.api.Borders(8).LineStyle = 1
    fg5.api.Borders(8).Weight = 3
    fg5.api.Borders(9).LineStyle = 1
    fg5.api.Borders(9).Weight = 3
    fg5.api.Borders(7).LineStyle = 1
    fg5.api.Borders(7).Weight = 3
    fg5.api.Borders(10).LineStyle = 1
    fg5.api.Borders(10).Weight = 3

    fg7 = worksheet.range("F19:G19")
    fg7.api.Merge()
    fg7.value = "事件管理经理签名:" + "name"
    fg7.api.Font.Size = 10
    fg7.api.Font.Name = "宋体"
    fg7.api.VerticalAlignment = -4108
    fg7.api.Borders(8).LineStyle = 1
    fg7.api.Borders(8).Weight = 3
    fg7.api.Borders(9).LineStyle = 1
    fg7.api.Borders(9).Weight = 3
    fg7.api.Borders(7).LineStyle = 1
    fg7.api.Borders(7).Weight = 3
    fg7.api.Borders(10).LineStyle = 1
    fg7.api.Borders(10).Weight = 3

def single_sheet_style():
    pass

def last_sheet_style():
    fg9 = worksheet.range("A20:G20")
    fg9.api.Merge()
    fg9.value = "表单保存单位:运维部 保存期限:3年 表单编号:ITSM-L4-020-001版本号V1.0"
    fg9.api.Font.Size = 9
    fg9.api.Font.Name = "宋体"
    fg9.api.RowHeight = 15
    fg9.api.VerticalAlignment = -4108

# elif i == 4:
# worksheet.range("B16").value = "30分钟"
# elif i == 5:
# worksheet.range("G16").value = "到场时间"
# elif i == 6:
# worksheet.range("B17").value = "解决时间"
# elif i == 7:
# worksheet.range("G17").value = "执行人"
head_sheet_style()
first_sheet_style()
hebing_sheet_style()
second_sheet_style()


last_sheet_style()






    # # 保存工作表
    # workbook.save("事件单.xlsx")
    # # 退出工作表
    # workbook.close()
    # # 关闭工作簿
    # app.quit()
