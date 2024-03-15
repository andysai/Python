# 导入模块
import tkinter as tk

windows = tk.Tk()
windows.title('my windows') # 设置标题
windows.geometry('480x320') # 设置长宽

text = tk.Entry(windows,show=None)
text.pack()

def insert_point():
    var = text.get()
    t.insert('insert',var)

def insert_end():
    var = text.get()
    t.insert('end',var)

b1 = tk.Button(windows,text='insert point',width=15,height=2,command=insert_point)
b1.pack()
b2 = tk.Button(windows,text='insert end',command=insert_end)
b2.pack()
t = tk.Text(windows,height=2)
t.pack()

windows.mainloop() # 循环
