# 报错后点击跳过
class Chinese:

    name = '吴枫'  # 类属性name

    def say(self):
        print(self.name + '是中国人')
        # 打印出'吴枫是中国人'
person = Chinese()
print(person.name)
person.say()