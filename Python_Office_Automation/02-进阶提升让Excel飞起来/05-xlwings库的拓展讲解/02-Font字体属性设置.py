"""
Font字体设置
    设置字体名称:Font.Name
        fg.api.Font.Name = "Arial"
    设置字体粗细:Font.Bold
        fg.api.Font.Bold = True
    设置字体大小:Font.Size
        fg.api.Font.Size = 20
    设置字体颜色:Font.Color
        # 先定义参数
        def get_rgb(r, g, b):
            return (2**16)*b+(2**8)*g+r
        fg.api.Font.Color = get_rgb(39,34,239)
"""
# 导入模块
import xlwings as xw

# 创建实例
app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")

# 打开工作表
worksheet = workbook.sheets['sheet1']

# 获取方格区域
fg = worksheet.range("B1:H6")

# 设置字体名称
fg.api.Font.Name = "宋体"

# 设置字体粗细
fg.api.Font.Bold = True

# 设置字体大小
fg.api.Font.Size = 20

# 设置字体颜色
def get_rgb(r, g, b):
    return (2**16)*b+(2**8)*g+r

fg.api.Font.Color = get_rgb(39, 34, 239)




