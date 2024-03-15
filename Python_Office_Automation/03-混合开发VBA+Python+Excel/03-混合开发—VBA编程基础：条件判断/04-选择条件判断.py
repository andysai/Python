"""
Dim number As Long
number = InputBox("请您输入抽奖编号")
Select Case number  # Select Case是一个关键字，后面放置一个变量
Case "2334" # 判断这个变量是否等于"2334"
    MsgBox "奖励一辆汽车"
Case "5643"
    MsgBox "奖励一本笔记本"
Case "3464"
    MsgBox "奖励一本书"
Case "5566"
    MsgBox "奖励一支笔"
Case Else # 以上条件都不满足的时候执行
    MsgBox "输入错误"
End Select # 最后结束判断
"""