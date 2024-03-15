"""
选择单元格
    1 选择当前工作表的单元格
        方式一
            activesheet.cells(5,4).select
        方式二
            activesheet.range("D5").select
        方式三
            [a3].select

    2 选择同一工作簿其他工作表的单元格(需要先激活当前工作表才可以使用 activate)
        方式一
            activeworkbook.worksheets("sheet2").cells(6,5).select
        方式二
            activeworkbook.worksheets("sheet2").range("a1:b3").select

    3 选择不同工作簿其他工作表的单元格
        方式一
            workbooks("薪资表.xlsm").worksheets("sheet2").range("a1:b3").select)
        方式二
            workbooks("薪资表.xlsm").worksheets("sheet2").activate
            activesheet.range("a1:b3").select

    4 选择与活动单元格相关的单元格
        activecell.offset(2,2).select

    5 选择与活动单元格不相关的单元格
        activesheet.cell(2,3).offset(5,4).select

    6 选择偏离指定区域的一个单元表格区域(先设置宏)
        activesheet.range("单元格范围b3c6").offset(4,3).select

    7 选择一个指定区域并扩展区域大小(先设置宏)
        activesheet.range("单元格范围b3c6").select
        selection.resize(selection.rows.count+5,selection.columns.count).select

"""