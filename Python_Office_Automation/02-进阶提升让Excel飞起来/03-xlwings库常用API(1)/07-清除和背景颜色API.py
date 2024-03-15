"""
range常用API
    获取指定方格的值:
        range("A1").value
    获取指定方格范围的值:
        range("A1:D4").value
    设置方格超链接
        fg.add_hyperlink(网址,显示名称,提示)
    获取当前方格地址
        fg.get_address()
    清除range的内容
        fg.clear_contents()
    清除格式和内容
        fg.clear()
    获取背景颜色
        fg.color
    给获取的颜色赋值:元组值
        fg.color = (12, 34, 125)
"""
import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xls")
sheet = workbook.sheets[0]
sheet.activate()

fg = sheet.range("A1:D4")

# for i in dir(fg):
#     print(i)

# fg.add_hyperlink("www.baidu.com", "百度", "链接到百度")
# fg.get_address()
# fg.clear_contents()
# fg.clear()
print(fg.color)
fg.color = (12, 34, 100)
print(fg.color) # None表示为空，即原来的颜色

