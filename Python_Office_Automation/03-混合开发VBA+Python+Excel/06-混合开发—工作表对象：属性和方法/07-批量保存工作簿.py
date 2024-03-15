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
        Workbooks.Add
        ActiveWorkbook.SaveAs (path)

    Next sh
End Sub

"""