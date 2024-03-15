"""
复制工作表到指定的工作簿
    visible:设置工作表可见
    worksheets("1月薪资表").visible=true
    复制工作表
        sheet1.copy after:=worksheets("bb.xls").sheets("sheet1") 跨表复制
"""

"""
Sub 工作表的分类汇总()
    '遍历1月份所有的工作表
    Dim sh As Worksheet
    '声明路径
    Dim path As String
    '声明工作簿名称
    Dim bookname As String
    
    For Each sh In Worksheets
        MsgBox sh.Name
        '指定创建路径
        path = "E:\study\python\Python_Office_Automation\03-混合开发VBA+Python+Excel\source_material\06\实战练习\" & sh.Name & ".xls"
        
        '创建工作簿文件
        Workbooks.Add
        ActiveWorkbook.SaveAs (path)
        bookname = sh.Name & ".xls"
        Select Case sh.Name
        Case "奖金表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        Case "考勤表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        Case "养老保险表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        Case "薪资表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        Case "医疗保险表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        Case "失业保险表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        Case "住房公积金"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        Case "工商保险表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        Case Else
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "1月" & sh.Name
        End Select
    Next sh
End Sub


"""