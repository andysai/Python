"""
第三方库:python-docx
安装:
    windows: pip install python-docx
    macos: pip3 install python-docx
使用方法:
    # 导入库
    from docx import Document
    # 创建word文档
    word = Document()
    # 加载原有后缀为docx的文档
    # path可以给绝对路径或者相对路径
    word = docx.Document(path)
"""