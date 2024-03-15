"""
Sub 密码验证()
    MsgBox "一共有三次机会!"
    Dim number As Long
    For number = 1 To 3
        If InputBox("请输入密码") = "233888" Then
            MsgBox "密码正确"
            Exit For
        Else
            MsgBox "已经使用" & number & "次机会"
        End If
    Next number
End Sub
"""