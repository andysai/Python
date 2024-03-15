# 导入库
import os
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt
# 设置字体颜色
from docx.shared import RGBColor

# 创建word文档
document = Document()

def get_filename(path, filetype):
    for filenames in os.walk(path):
        print(filenames[2])

# python程序执行入口
if __name__ == "__main__":
    # 切换目录
    path = "../source_material/01/text文档"
    os.chdir(path)

    # 获取目录下的文本
    get_filename(".", ".txt")
