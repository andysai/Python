# 导入tk模块
import tkinter as tk

class MyApp(object):
    # 1 定义主界面函数
    def __init__(self, parent):
        self.root = parent
        self.root.title("信息节点端口查询")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        # 1.1 信息点查找端口
        check_message = tk.Button(root, text='1 信息点查找端口', width=16, height=2, command=self.find_message)
        check_message.place(x=100, y=160, anchor="c")

        # 1.2 端口号查找信息点
        check_port = tk.Button(root, text='2 端口号查找信息点', width=16, height=2, command=self.find_port)
        check_port.place(x=240, y=160, anchor="c")

        # 1.3 退出软件
        close = tk.Button(root, text='3 退出', width=16, height=2, command=root.quit)
        close.place(x=380, y=160, anchor="c")

    # 2 窗口切换
    def hide(self):
        self.root.withdraw()

    # 3 定义信息节点
    def find_message(self):
        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.title("信息节点端口查询")
        screenWidth= otherFrame.winfo_screenwidth()
        screenHeight = otherFrame.winfo_screenheight()
        width = 480
        height = 320
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        otherFrame.geometry("%dx%d+%d+%d" % (width, height, left, top))
        handler = lambda: self.onCloseOtherFrame(otherFrame)

        # 3.1 定义用户输入文本框参数
        l = tk.Label(otherFrame, text="输入节点信息")
        l.pack()
        user_text = tk.Entry(otherFrame, show=None,width=25)
        user_text.pack()

        # 3.2 定义输出文本框参数
        l = tk.Label(otherFrame, text="输出节点信息")
        l.pack()
        lb = tk.Text(otherFrame, height=2,width=25)
        lb.pack()

        # 3.3 信息节点查询
        def Query_information():
            user = user_text.get()
            Information_point = int(user)
            if Information_point > 0 and Information_point <= 49:
                position = Information_point - 1 + 1
                result = f'该信息节点在第一台交换机，对应端口号为:{position}'
                lb.insert('end', result)
            elif Information_point > 49 and Information_point <= 96:
                position = Information_point - 49 + 1
                result = f'该信息节点在第二台交换机，对应端口号为:{position}'
                lb.insert('end', result)
            elif Information_point > 96 and Information_point <= 144:
                position = Information_point - 97 + 1
                result = f'该信息节点在第三台交换机，对应端口号为:{position}'
                lb.insert('end', result)
            elif Information_point > 144 and Information_point <= 192:
                position = Information_point - 145 + 1
                result = f'该信息节点在第四台交换机，对应端口号为:{position}'
                lb.insert('end', result)
            elif Information_point > 192 and Information_point <= 240:
                position = Information_point - 193 + 1
                result = f'该信息节点在第五台交换机，对应端口号为:{position}'
                lb.insert('end', result)
            else:
                lb.insert('end', '请输入正确的信息节点!')

        # 3.4 清空文本框内容
        def clear_message():
            user_text.delete(0, 'end')
            lb.delete(1.0, 'end')

        # 3.5 查找按钮
        check = tk.Button(otherFrame, text='查找', width=10, height=2, command=Query_information)
        check.place(x=96, y=240, anchor="c")

        # 3.6 清空按钮
        clear = tk.Button(otherFrame, text='清空', width=10, height=2, command=clear_message)
        clear.place(x=288, y=240, anchor="c")

        # 3.7 关闭按钮
        close = tk.Button(otherFrame, text='关闭', width=10, height=2, command=otherFrame.quit)
        close.place(x=192, y=240, anchor="c")

        # 3.8 返回
        reset = tk.Button(otherFrame, text='返回', width=10, height=2, command=handler)
        reset.place(x=384, y=240, anchor="c")

    # 4 定义端口信息
    def find_port(self):
        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.title("信息节点端口查询")
        screenWidth= otherFrame.winfo_screenwidth()
        screenHeight = otherFrame.winfo_screenheight()
        width = 480
        height = 320
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        otherFrame.geometry("%dx%d+%d+%d" % (width, height, left, top))
        handler = lambda: self.onCloseOtherFrame(otherFrame)

        # 4.1 定义用户输入文本框参数
        l = tk.Label(otherFrame, text="输入交换机编号")
        l.pack()
        user_text1 = tk.Entry(otherFrame, show=None,width=25)
        user_text1.pack()
        l = tk.Label(otherFrame, text="输入端口信息")
        l.pack()
        user_text2 = tk.Entry(otherFrame, show=None,width=25)
        user_text2.pack()

        # 4.2 定义输出文本框参数
        l = tk.Label(otherFrame, text="输出节点信息")
        l.pack()
        user_text3 = tk.Entry(otherFrame, show=None,width=25)
        user_text3.pack()

        # 4.3 端口号查询信息点
        def switch_port_message():
            user1 = user_text1.get()
            switch = int(user1)
            user2 = user_text2.get()
            Port_number = int(user2)
            if (Port_number >= 1 and Port_number <= 48) and switch == 1:
                position = Port_number
                result = f'信息点为{position}'
                user_text3.insert('end',result)
            elif (Port_number >= 1 and Port_number <= 48) and switch == 2:
                position = Port_number + 49 - 1
                result = f'信息点为{position}'
                user_text3.insert('end',result)
            elif (Port_number >= 1 and Port_number <= 48) and switch == 3:
                position = Port_number + 97 - 1
                result = f'信息点为{position}'
                user_text3.insert('end',result)
            elif (Port_number >= 1 and Port_number <= 48) and switch == 4:
                position = Port_number + 145 - 1
                result = f'信息点为{position}'
                user_text3.insert('end',result)
            elif (Port_number >= 1 and Port_number <= 48) and switch == 5:
                position = Port_number + 193 - 1
                result = f'信息点为{position}'
                user_text3.insert('end',result)
            else:
                user_text3.insert('end', "请输入正确的交换机编号和端口号")

        # 4.4 清空文本框内容
        def clear_message():
            user_text1.delete(0, 'end')
            user_text2.delete(0, 'end')
            user_text3.delete(0, 'end')

        # 4.5 查找按钮
        check = tk.Button(otherFrame, text='查找', width=10, height=2, command=switch_port_message)
        check.place(x=96, y=240, anchor="c")

        # 4.6 清空按钮
        clear = tk.Button(otherFrame, text='清空', width=10, height=2, command=clear_message)
        clear.place(x=288, y=240, anchor="c")

        # 4.7 关闭按钮
        close = tk.Button(otherFrame, text='关闭', width=10, height=2, command=otherFrame.quit)
        close.place(x=192, y=240, anchor="c")

        # 4.8 返回
        reset = tk.Button(otherFrame, text='返回', width=10, height=2, command=handler)
        reset.place(x=384, y=240, anchor="c")

    # 5 切换窗口
    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

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
