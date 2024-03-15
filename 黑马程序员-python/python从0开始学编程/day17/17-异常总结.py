"""
总结
    异常语法:
        try:
            可能发生异常的代码
        except:
            如果出现异常执行的代码
        else:
            没有发生异常执行的代码
        finally:
            无论是否异常都要执行的代码
    捕获异常:
        except:
            代码

        except 异常类型 as xx:
            代码
    自定义异常:
        # 1 自定义异常类
            class 异常类类名(Exception):
                代码

                # 设置抛出异常的描述信息
                def __srtr__(self):
                    return ...
        # 2 抛出异常
        raise 异常类名()
        # 3 捕获异常
        except Exception...
"""