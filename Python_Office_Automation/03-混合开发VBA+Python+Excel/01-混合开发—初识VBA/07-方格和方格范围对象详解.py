"""
worksheets表示当前所打开工作表的集合-集合演示
    1.单个方格对象:[a1] 如果取值就调用value属性，可读可写
        Worksheets("1月薪资表").[a1].value = 100
    2.xlwings中的表示方法:range("A1:B2") value属性取值，可读可写
        Worksheets("1月薪资表")Range("a1").value = 100
    3.单个方格对象:cells(行号, 列号) value属性取值，可读可写
        Worksheets("1月薪资表").Cells(3,3).value = 100
"""