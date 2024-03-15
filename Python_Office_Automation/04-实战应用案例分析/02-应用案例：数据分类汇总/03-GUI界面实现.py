# 导入模块
from tkinter import *

# 创建窗体
# 创建TK对象
root = Tk()
# 设置标题
root.title("数据筛选")
# 设置窗体大小
root.geometry("400x60")

# 设置一个单行输入框
entry = Entry(root)
# 设置输入框
entry.pack(side=LEFT)

# 编写函数
def bumen():
    print("部门")

def xinzi():
    print("薪资")

def jiangjin():
    print("奖金")

# 设置按钮并设置位置
Button(root, text="部门", command=bumen).pack(side=LEFT)
Button(root, text="薪资", command=xinzi).pack(side=LEFT)
Button(root, text="奖金", command=jiangjin).pack(side=LEFT)

# tk的mainloop方法
root.mainloop()
