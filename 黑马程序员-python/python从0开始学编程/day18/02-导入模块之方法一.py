"""
导入模块的方式
    import 模块名
    from 模块名 import 功能名
    from 模块名 import *
    import 模块名 as 别名
    from 模块名 import 功能名 as 别名


语法:
    # 1 导入模块
    import 模块名
    import 模块名1,模块名2  # 不建议这种写法

    # 2 调用功能
    模块名.功能名()
"""
# 需求:math模块下sqrt()开平方计算
"""
1 导入模块
2 测试是否导入成功:调用该模块内的sqrt功能
"""
import math
print(math.sqrt(9)) # 3.0