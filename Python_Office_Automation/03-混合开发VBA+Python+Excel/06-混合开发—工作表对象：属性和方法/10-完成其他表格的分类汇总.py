"""
Sub 工作表的分类汇总()
    '遍历2月份工作表，并创建工作簿文件
    Dim sh As Worksheet
    Dim bookname As String

    For Each sh In Worksheets
        '拼接表名
        bookname = sh.Name & ".xls"
        'MsgBox path
        Select Case sh.Name
        Case "奖金表"
          sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
          ActiveSheet.Name = "2月" & sh.Name
        Case "考勤表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "2月" & sh.Name
        Case "养老保险表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "2月" & sh.Name
        Case "薪资表"
             sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
             ActiveSheet.Name = "2月" & sh.Name
        Case "医疗保险表"
             sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
             ActiveSheet.Name = "2月" & sh.Name
        Case "失业保险表"
             sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
             ActiveSheet.Name = "2月" & sh.Name
        Case "住房公积金"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "2月" & sh.Name
        Case "工商保险表"
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "2月" & sh.Name
        Case Else
            sh.Copy before:=Workbooks(bookname).Sheets("sheet1")
            ActiveSheet.Name = "2月" & sh.Name
        End Select
    Next sh

End Sub


"""