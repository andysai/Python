from tkinter import *
root = Tk() #调用窗口
root.title('快递查询') #设置标题
root.geometry('500x500') # 设置窗口大小
root.resizable(width=False,height=False)
E1 = Entry(root)
E1.place(width=250, height=30)
root.mainloop()