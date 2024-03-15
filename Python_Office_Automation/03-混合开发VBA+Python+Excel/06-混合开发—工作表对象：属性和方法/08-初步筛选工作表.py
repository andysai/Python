"""
Sub 工作表的分类汇总()
    '遍历1月份所有的工作表
    Dim sh As Worksheet
    '声明路径
    Dim path As String

    For Each sh In Worksheets
        MsgBox sh.Name
        '指定创建路径
        path = "E:\study\python\Python_Office_Automation\03-混合开发VBA+Python+Excel\source_material\06\实战练习\" & sh.Name & ".xls"

        '创建工作簿文件
        'Workbooks.Add
        'ActiveWorkbook.SaveAs (path)

        Select Case sh.Name
        Case "奖金表"
            MsgBox "复制奖金表"
        Case "考勤表"
            MsgBox "复制考勤表"
        Case "养老保险表"
            MsgBox "复制养老保险表"
        Case "薪资表"
            MsgBox "复制薪资表"
        Case "医疗保险表"
            MsgBox "复制医疗保险表"
        Case "失业保险表"
            MsgBox "复制失业保险表"
        Case "住房公积金"
            MsgBox "复制住房公积金"
        Case "工商保险表"
            MsgBox "复制工商保险表"
        Case Else
            MsgBox "复制剩余保险表"
        End Select
    Next sh
End Sub

"""