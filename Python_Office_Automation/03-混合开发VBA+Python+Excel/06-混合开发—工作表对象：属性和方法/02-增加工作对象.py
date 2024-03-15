"""
新增工作表
    add:创建新的工作表，并会自动命名
        worksheets.add
    add.name:新增一个工作表，命名为:2约薪资
        worksheets.add.name = "2月薪资"
    add after:新增一个工作表，指定放在某个工作表之后
        worksheets.add after:=worksheets("1月薪资表")
    add before:新增一个工作表，指定放在某个工作表之前
        worksheets.add before:=worksheets("1月薪资表")

新增和删除工作表
    count:指定新增工作表的数量
        worksheets.add before:=worksheets("1月薪资表"),count:=3
    delete:指定删除工作表
        worksheets(2).delete
"""