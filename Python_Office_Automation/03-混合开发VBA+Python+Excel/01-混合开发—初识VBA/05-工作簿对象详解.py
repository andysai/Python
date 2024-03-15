"""
workbooks表示当前所打开工作簿的集合-集合演示
    1.以序号表示:workbooks(1)
        Msgbox Workbooks(序号).Name #查看当前工作簿的名称
    2.以全名称表示:workbooks("新工作簿01.xlsx")
        Msgbox Workbooks("工作簿名称").Name
    3.当前工作簿表示(写VBA程序的工作簿):ThisWorkbook
        Msgbox ThisWorkbook.Name
    4.活动工作簿表示(最前面的工作簿):ActiveWorkbook
        Msgbox ActiveWorkbook.Name
"""