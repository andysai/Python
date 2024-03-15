"""
递归
    函数内部自己调用自己
    必须有出口
lambda
    语法
        lambda 参数列表：表达式
    lambda的参数形式
        无参数
            lambda：表达式
        一个参数
            lambda 参数 : 表达式
        默认参数
            lambda key=value : 表达式
        不定长位置参数
            lambda **args : 表达式
        不定长关键字参数
            lambda **kwargs : 表达式

高阶函数
    作用:把函数作为参数传入，化简代码
    内置高阶函数
        map()
        reduce() # 需要导入functools才可以使用
        filter()
"""