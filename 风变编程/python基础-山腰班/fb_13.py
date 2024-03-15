"""
要让机器人跟我们打招呼，至少要告诉 ta 两个信息：一是 ta 的名字，二是你的称呼。
请你根据课堂所学（初始化方法即可）及之前已经掌握的知识，让 ta 先和你打个招呼。

假设你说了一个愿望：学会 Python 基础！
那么，机器人就会复述如下：

**（你的称呼）的愿望是：
学会 Python 基础！
学会 Python 基础！
学会 Python 基础！
这个功能可以用一个实例方法来实现，可命名为“say_wish”。
"""

class Say_Hello :
    def __init__(self,RobotName,MyName,wish):
        self.RobotName = RobotName
        self.MyName = MyName
        self.wish = wish

    def Hello(self):
        mess = '你好，{}。我是{}。遇见你，真好。'.format(self.MyName,self.RobotName)
        return mess

    def Say_Wish(self):
        mess1 = '{}的愿望是：\n{}'.format(self.MyName,self.wish*3)
        return mess1

test = Say_Hello('瓦力','sai','学会 Python 基础！\n')
print(test.Hello())
print(test.Say_Wish())


