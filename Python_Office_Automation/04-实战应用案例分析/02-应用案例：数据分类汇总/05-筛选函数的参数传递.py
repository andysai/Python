# 导入模块
from tkinter import *
import xlwings as xw

# 创建窗体
def set_gui(workbook):
    str_name = ['部门', '薪资', '奖金']
    # 创建TK对象
    root = Tk()
    # 设置标题
    root.title("数据筛选")
    # 设置窗体大小
    root.geometry("400x60")

    # 设置一个单行输入框
    entry = Entry(root)
    # 设置输入框
    entry.pack(side=LEFT)

    # 编写函数
    def bumen():
        get_value = entry.get()
        # 执行筛选功能
        shaixuan(workbook, get_value, str_name[0])

    def xinzi():
        get_value = entry.get()
        # 执行筛选功能
        shaixuan(workbook, get_value, str_name[1])

    def jiangjin():
        get_value = entry.get()
        # 执行筛选功能
        shaixuan(workbook, get_value, str_name[2])

    # 设置按钮并设置位置
    Button(root, text=str_name[0], command=bumen).pack(side=LEFT)
    Button(root, text=str_name[1], command=xinzi).pack(side=LEFT)
    Button(root, text=str_name[2], command=jiangjin).pack(side=LEFT)

    # tk的mainloop方法
    root.mainloop()

# python程序执行入口
if __name__ == "__main__":
    # 打开原有工作簿
    app = xw.App(visible=Tk, add_book=False)
    workbook = app.books.open("../source_material/02/数据筛选.xlsx")

    # 创建操作界面
    set_gui()
