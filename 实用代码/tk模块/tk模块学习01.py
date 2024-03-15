# 导入模块
import tkinter as tk

windows = tk.Tk()
windows.title('my windows') # 设置标题
windows.geometry('480x320') # 设置长宽

var = tk.StringVar()
l = tk.Label(windows, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
l.pack()  # 展示位置
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        var.set('')


b = tk.Button(windows,text='hit me',width=15,height=2,command=hit_me)
b.pack()

windows.mainloop() # 循环
