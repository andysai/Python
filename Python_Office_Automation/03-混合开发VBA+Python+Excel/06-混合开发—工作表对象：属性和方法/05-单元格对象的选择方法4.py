"""
range属性
    range("A1") 单元格A1
    range("A1:B5") 从单元格A1到单元格B5的区域
    range("C5:D9,G9:H16") 多块选定区域
    range("A:A") A列
    range("1:1") 第1行
    range("A:C") 从A列到C列的区域
    range("1:5") 从第1行到第5行的区域
    range("1:1,3:3,8:8") 第1、3、8行
    range("A:A,C:C,F:F") A、C和F列
行和列属性
    rows(1) 第1行
    rows 工作表上所有的行
    columns(1) 第1列
    columns("A") 第1列
    columns 工作表上所有的列
联合方法
    union(rows(1),rows(3),rows(5)) 第1行、第3行、第5行
    union(columns(1),columns(2),columns(5)) 第1列、第2列、第5列
"""