"""
删除和复制工作表
    activate:激活某个工作表(设置某个工作表为活动工作表，只能有1个活动工作表)
        worksheets("sheet2").activate
    copy:复制工作表，谁调用就表示复制谁
        worksheets("1月薪资表").copy
    copy before:复制工作表，并复制到指定工作表的前面
        worksheets("1月薪资表").copy before :=worksheets("1月薪资表")
    copy after:复制工作表，并复制到指定工作表的后面
        worksheets("1月薪资表").copy after:=worksheets("1月薪资表")
"""