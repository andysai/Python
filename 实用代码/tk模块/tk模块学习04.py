# 导入模块
import tkinter as tk

windows = tk.Tk()
windows.title('my windows') # 设置标题
windows.geometry('480x320') # 设置长宽

var = tk.StringVar()
l = tk.Label(windows,bg='yellow',width=20,text='empty')
l.pack()

def print_selecton():
    l.config(text='you have selected' + var.get())

rl = tk.Radiobutton(windows,text='Option A', variable=var,value='A',command=print_selecton)
rl.pack()

windows.mainloop() # 循环
