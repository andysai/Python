# 导入模块
from docx import Document
import os
import shutil

# 获取所有的路径信息
def get_filepth(path, filetype):
    for root, dirs, files in os.walk(path):
        return files

# 设置文件名
def set_file_name(path, file_name):
    for file_single in file_name:
        # 循环加载原有文档
        document = Document(path + "/" + file_single)
        file_name_str = document.paragraphs[0].text
        path1 = "../source_material/04/03一键给word文档命名/未命名的word文档/命名后的文件/"
        old_name = path + "/" + file_single
        new_name = path1 + file_single
        shutil.copyfile(old_name, new_name)

        os.rename(path1 + file_single, path1 + file_name_str + ".docx")

# 程序执行入口
if __name__ == '__main__':
    # 获取所有的路径信息
    path = "../source_material/04/03一键给word文档命名/未命名的word文档/原始文件"
    file_name = get_filepth(path, ".docx")
    print(file_name)

    # 设置文件名
    set_file_name(path, file_name)
