# 导入模块
import tkinter as tk

windows = tk.Tk()
windows.title('my windows') # 设置标题
windows.geometry('480x320') # 设置长宽

l = tk.Label(windows,text='',bg='yellow')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do' + str(counter))
    counter += 1

menubar = tk.Menu(windows)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=do_job)
filemenu.add_command(label="Open",command=do_job)
filemenu.add_command(label="Save",command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=windows.quit)

windows.config(menu=menubar)
windows.mainloop() # 循环
