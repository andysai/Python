# 1 自定义异常类，继承Exception，魔法方法有init和str(设置异常描述信息)
class ShortInputError(Exception):
    def __init__(self, lenght, min_len):
        # 用户输入的密码长度
        self.lenght = lenght
        # 系统要求的最少长度
        self.min_len = min_len

    # 设置异常描述信息
    def __int__(self):
        return f'您输入的密码长度是{self.lenght},密码不能少于{self.min_len}'

# 2 抛出异常
# 3 捕获该异常