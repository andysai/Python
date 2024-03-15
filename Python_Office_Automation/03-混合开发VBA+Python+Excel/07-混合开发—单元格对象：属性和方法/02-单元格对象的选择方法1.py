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

"""