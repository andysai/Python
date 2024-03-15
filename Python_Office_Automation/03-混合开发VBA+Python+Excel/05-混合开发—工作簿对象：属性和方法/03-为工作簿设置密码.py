"""
Sub 设置工作簿密码()

    Dim wb As Workbook
    Set wb = Workbooks(1)
    wb.Password = InputBox("请输入文档的设定密码", "设定密码")
    wb.Save
    wb.Close
    MsgBox "密码设定成功"

End Sub

"""