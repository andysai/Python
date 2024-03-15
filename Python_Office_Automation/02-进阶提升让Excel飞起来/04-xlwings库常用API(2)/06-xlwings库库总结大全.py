"""
1.xlwings库安装
    pip install xlwings
    安装过程注意问题:因为第三方库不在国内，可能会出现网络问题，这个时候更换网络，尝试连接手机热点解决
2.启动app应用
    app = xw.App(visible = True, add_book = False)
    相当于是启动应用图标的作用
3.Bool工作簿API
    3.1.打开原工作簿(相对路径)
        wprkbook = app.books.open("文件路径")
    3.2.创建新工作簿(需要对新创建工作簿进行相对路径保存)
        workbook = app.books.add()
        保存工作簿(有2种方式)
        方式1:另存为:workbook.save("文件路径")
        方式2:workbook.save()
        关闭工作簿(实际上是退出所有的工作表)
        workbook.close()
        退出工作簿
        app.quit()
4.Sheet工作表API
    4.1 获取所有工作表
        listsht = workbook.sheets
        返回一个列表，列表中存放的都是工作表对象
    4.2 打开原工作表(有2种方式)
        方式1:工作表名称
            sheet = workbook.sheets["sheet1"]
        方式2:工作表下表
            sheet = workbook.sheets[0]
    4.3 激活活动表格
        sheet.activate() 将当前的工作表设置为当前我们能看到的工作表
    4.4 表格的清除
        清除表格的内容和格式
        sheet.clear()
        清除表格的内容
        sheet.clear_contents()
        删除表格
        sheet.delete()
5.Range工作表API
    5.1 方格或者是方格范围对象
        获取当前的方格对象或者是方格范围对象
        fg = sheet.range(范围字符串)
        范围字符串:比如:"A1"或者"A1:H5"
    5.2 超链接
        添加超链接:fg.add_hyperlink(网址,显示名称,提示)
        设定超链接:fg.hyperlink = 网址
    5.3 获取方格或方格范围地址
        get_address()
    5.4 清除内容
        # 清除range的内容
        fg.clear_contents()
        # 清除格式和内容
        fg.clear()
    5.5 设定颜色
        # 获取背景颜色
        fg.color
        # 给获取的颜色赋值:元组值
        fg.color = (234,33,56)
    5.6 column列所表示的意义
        column 返回所在的列标
        columns 返回指定范围的列对象(不是值，是对象)
        取值范围:fg.columns[下标]
        长度属性:len(fg.columns)
        column_width # 只能返回1列的列宽,不能返回多列,多列为空
        fg.column_width = 50
    5.7 row行所表示的意义
        row 返回所在的行标
        rows 返回指定范围的行对象(不是值，是对象)
        取值范围:fg.rows[下标]
        长度属性:len(fg.rows)
        row_width # 只能返回单行的行高,不能返回多行,多行为空
        fg.row_height = 50
    5.8 row行所表示的意义
        # 自动调整行高列宽
        fg.autofit
6.类和对象的属性和方法查看方式
    1 dir(类名或者对象名)
    2 help(类名或者对象名)
    第三方的源码查看方法
    1 库名__file__
"""