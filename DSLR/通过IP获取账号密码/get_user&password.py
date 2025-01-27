# 导入tk模块
import tkinter as tk

class MyApp(object):
    # 1 定义主界面函数
    def __init__(self, parent):
        self.root = parent
        self.root.title("通过IP获取账号密码")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        # 4.4 清空文本框内容
        # def clear_message():
        #     user_text1.delete(0, 'end')
        #     user_text2.delete(0, 'end')
        #     user_text3.delete(0, 'end')


        # 1.2 定义用户输入文本框参数
        l = tk.Label(root, text="输入IP信息")
        l.pack()
        user_text = tk.Entry(root, show=None,width=25)
        user_text.pack()

        # 1.3 定义输出文本框参数
        l = tk.Label(root, text="输出账户信息")
        l.pack()
        lb = tk.Text(root, height=2, width=25)
        lb.pack()

        l = tk.Label(root, text="输出密码信息")
        l.pack()
        lb = tk.Text(root, height=2, width=25)
        lb.pack()

        # 通过ip获取账号密码信息
        def find_IP_message():
            ip = user_text.get()
            with open('a.txt', 'r',encoding='utf-8') as f:
                if ip in f.readlines()[0]:
                    print(f.readlines()[1])


        # 1.1 查询IP地址
        check_message = tk.Button(root, text='1 查询', width=13, height=2, command=find_IP_message)
        check_message.place(x=100, y=200, anchor="c")

        # 4.6 清空按钮
        clear = tk.Button(root, text='2 清空', width=13, height=2)
        clear.place(x=240, y=200, anchor="c")

        # 1.4 退出软件
        close = tk.Button(root, text='3 退出', width=13, height=2, command=root.quit)
        close.place(x=380, y=200, anchor="c")




    # 6 更新数据
    def show(self):
        self.root.update()
        self.root.deiconify()

# 7 调用函数
if __name__ == "__main__":
    root = tk.Tk()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    width = 480
    height = 320
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2
    root.geometry("%dx%d+%d+%d" % (width, height, left, top))
    app = MyApp(root)
    root.mainloop()
