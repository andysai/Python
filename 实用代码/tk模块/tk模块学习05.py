# 首先导入tk
import tkinter as tk

# 定义窗口
window = tk.Tk()

window.title('BIN信息管理系统')

window.geometry('600x400')

# 定义一个输入文本框
# entry = tk.Entry(window, show="*")
# 表示输入的字符以*号的形式出现
entry = tk.Entry(window, show=None)
# 对文本框内容进行打包
entry.pack()


# 定义一个插入在鼠标所在位置的函数
def insert_point():
    var = entry.get()
    t.insert('insert', var)


# 定义按钮
b1 = tk.Button(window, text='插入到指定位置', width=15, height=2, command=insert_point)
# 打包按钮
b1.pack()

window.mainloop()