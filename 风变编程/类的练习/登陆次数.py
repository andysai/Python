# 9-5 尝试登陆次数：在9-3编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加。
# 再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的值重置为0.
#根据User类创建一个实例，再调用方法increment_login_attempts()多次。
# 打印属性login_attempts的值，确认它被正确地递增；
# 然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。
class User:
    def __init__(self, first_name, last_name, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        return '你好，我的名字叫%s,年龄是:%d,喜欢的食物是:%s,兴趣爱好是:%s' % ((self.first_name+self.last_name),self.age,self.food,self.interest)

    def greet_user(self):
        return '你好，%s\n' % (self.first_name+self.last_name)

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

user = User('mark', 'sun')
user.greet_user()
# 调用方法递增登录次数
for i in range(5):
    user.increment_login_attempts()
print("You have login " + str(user.login_attempts) + " times.")  # 验证登录次数被正确递增
user.reset_login_attempts()  # 调用方法重置登录次数
print("You login " + str(user.login_attempts) + " time.")  # 确认登录次数被重置