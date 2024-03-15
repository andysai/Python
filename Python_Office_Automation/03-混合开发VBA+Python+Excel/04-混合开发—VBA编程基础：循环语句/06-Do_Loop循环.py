"""
无限循环-退出为exit do
Sub text()
    Dim number As Integer
    number = 0
    Do
        number = number + 1
        MsgBox number
        If number = 3 Then
         Exit Do
        End If
    Loop

End Sub

"""