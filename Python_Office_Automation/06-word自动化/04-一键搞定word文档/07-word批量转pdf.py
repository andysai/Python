import win32com.client
import pythoncom
import os

# pip install pywin32

class Word_to_PDF(object):

    def __init__(self, filepath, Debug=False):
        self.wordApp = win32com.client.Dispatch('word.Application')
        self.wordApp.Visible = Debug
        self.myDoc = self.wordApp.Documents.Open(filepath)

    # 进行转化的操作
    def export_pdf(self, output_file_path):
        self.myDoc.ExportAsFixedFormat(output_file_path, 17, Item=7, CreateBookmarks=0)

    # 执行完关闭程序
    def close(self):
        self.wordApp.Quit()

# 定义程序执行入口
if __name__ == '__main__':
    path = "../source_material/04/05一键批量word转pdf"
    os.chdir(path)
    rootpath = os.getcwd()  # 获取当前的py文件所在的文件夹路径
    save_path = os.getcwd()  # PDF储存位置

    pythoncom.CoInitialize()

    os_dict = {root: [dirs, files] for root, dirs, files in os.walk(rootpath)}
    for parent, dirnames, filenames in os.walk(rootpath):
        for filename in filenames:
            if u'.doc' in filename and u'~$' not in filename:
                # 直接保存为PDF文件

                a = Word_to_PDF(rootpath + '\\' + filename, True)

                title = filename.split('.')[0]  # 删除.docx
                str_adress = rootpath + '\\' + "pdf存储位置\\" + title + '.pdf'
                print(str_adress)

                a.export_pdf(str_adress)

    print('已经转化完成了，你很棒')
