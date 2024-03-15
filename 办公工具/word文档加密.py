# 导入库
import win32com.client
import time

# 添加加密的密码
password = input("请输入加密密码:")
# 原始文件路径
# path1 = r"E:\study\python\实用代码\python学习计划.docx"
path1 = input("请输入需要进行加密文档的路径:")
# 加密后文件路径
# path2 = r"E:\study\python\实用代码\python学习计划2.docx"
old_path1 = path1
first_path2 = ",".join(old_path1.split("\\")[:-1]).replace(",", "\\") + "\\"
second_path2 = old_path1.split("\\")[-1][:-5] + "_new.docx"
path2 = first_path2 + second_path2

# 创建方法
word_app = win32com.client.Dispatch("Word.Application")
# 后台运行，不显示，不警告
word_app.Visible = 0
word_app.DisplayAlerts = 0
# 读取原始文件
doc = word_app.Documents.Open(path1)
# 保存为新文件
doc.SaveAs(path2, None, False, password, True, "", False, False, False, False)
# 退出
word_app.Quit()

print("执行成功")
# 显示时间
time.sleep(5)
