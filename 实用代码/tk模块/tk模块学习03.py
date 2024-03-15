# 导入模块
import tkinter as tk

windows = tk.Tk()
windows.title('my windows') # 设置标题
windows.geometry('480x320') # 设置长宽

var1 = tk.StringVar()
l = tk.Label(windows,bg='yellow',width=4,textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(windows,text='print selection',width=15,height=2,command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(windows,listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

windows.mainloop() # 循环
