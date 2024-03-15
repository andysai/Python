import tkinter as tk
from tkinter import *
import requests
from bs4 import BeautifulSoup

# 面向对象的编程思想
class APP:
    def __init__(self, master):
        # 自动选定大小与位置
        self.frame = tk.Frame(master)
        self.frame.pack()
        # 窗口内容设置
        l = tk.Label(self.frame,
                     text='欢迎使用MAC地址转换工具',  # 标签的文字
                     font=('Arial', 12),  # 字体和字体大小
                     width=25, height=2  # 标签长宽
                     )
        l.pack()

        # 设置一个文本框
        self.user_text = tk.Entry(self.frame,font=('Arial', 12))
        self.user_text.pack()

        # 新建一个按钮
        # 自动设置按钮的位置
        self.hi_there = tk.Button(self.frame,
                                  text="转换",
                                  command=self.get_organization)
        self.hi_there.pack()

        self.listb = Listbox(self.frame,selectmode=MULTIPLE,height=3,width=25)
        self.listb.pack()


    def getuser(self):
        return self.user_text.get()

    def _introduce(self):
        mac_address = self.getuser()

        mac_address_list = []

        for i in mac_address:
            mac_address_list.append(i)

        mac_address_list[2:0] = '-'
        mac_address_list[8:0] = '-'
        mac_address_list[14:0] = '-'
        mac_address_str = "".join(str(i) for i in mac_address_list).replace('.', '-')
        return mac_address_str
        #print(mac_address_str)
        #self.listb.delete(0)
        #self.listb.insert(0,self._introduce)

    def get_organization(self):
        url = 'https://mac.51240.com/' + self._introduce() + '__mac/'
        headers = {
            'user-agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.25Safari / 537.36Core / 1.70.3741.400QQBrowser / 10.5.3863.400'
            # 标记了请求从什么设备，什么浏览器上发出
        }
        res = requests.get(url, headers=headers)
        mes = res.status_code  # 查看网页状态
        suop = BeautifulSoup(res.text, 'html.parser')
        web = suop.find_all('tr')
        message = []
        for tr in web:
            num = tr.find('td', bgcolor='#FFFFFF').text
            if num not in message:
                message.append(num)
        organization_name = message[1]
        #return organization_name
        print(organization_name)
        #self.listb.delete(0)
        self.listb.insert(0,self.get_organization)


def main():
    window = tk.Tk()

    window.title('MAC地址转换')
    window.geometry('250x250')
    app = APP(window)

    window.mainloop()

if __name__ == '__main__':
    main()

