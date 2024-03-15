from tkinter import *

def Express_inquiry():
    Courier_number = ''
    return Courier_number

def GUI():
    root = Tk() #调用窗口
    root.title('快递查询') #设置标题
    root.geometry('500x500') # 设置窗口大小
    root.resizable(width=False,height=False)
    E1 = Entry(root)
    E1.place(width = 15,height = 2)
    E1.pack()
    button1=Button(root,text='查询',command=Express_inquiry,width=15,height=2,relief=FLAT)
    button1.pack()
    Label(root,E1).pack(fill=Y,expand=1,side=LEFT)
    Label(root, button1).pack(fill=X, expand=1, side=RIGHT)
    root.mainloop()


if __name__ == '__main__' :
    GUI()