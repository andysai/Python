# 导入模块
import win32com.client
import pythoncom
import os

class Word_to_PDF(object):
    def __init__(self, filepath, Debug=False):
        """
        filepath 表示文件路径:
        Debug: 控制过程是否可视化，True为可视化，False不可视化
        """
        self.workApp = win32com.client.Dispatch("word.Application")
        self.workApp.Visible = Debug
        self.myDoc = self.workApp.Documents.Open(filepath)

    # 进行转化
    def export_pdf(self, output_file_path):
        self.myDoc.ExportAsFixedFormat(output_file_path, 17, Item=7, CreateBookmarks=0)

    # 执行完关闭程序
    def close(self):
        self.workApp.Quit()

# 定义程序执行入口
if __name__ == "__main__":
    path = "../source_material/04/02 一键批量转pdf"
    os.chdir(path)
    rootpath = os.getcwd() # 获取当前的py文件所在的文件夹路径
    save_path = os.getcwd() # PDF储存位置
    pythoncom.CoInitialize()

    os_dict = {root:[dirs, files] for root, dirs, files in os.walk(rootpath)}
    for parent, dirnames, filenames in os.walk(rootpath):
        for filename in filenames:
            if u'.doc' in filename and u'~$' not in filename:
                # 直接保存为PDF文件
                a = Word_to_PDF(rootpath + '/' + filename, True)

                title = filename.split('.')[0] # 删除.docx
                str_address = rootpath + '/' + "pdf存储位置/" + title + ".pdf"
                print(str_address)

                a.export_pdf(str_address)
    print("已经转化完成了，你很棒")
