from docx import Document

# 加载原有文档，绝对或者相对路径都可以
document = Document("../source_material/02/A/python简介.docx")

for paragraph in document.paragraphs:
    print(paragraph.text)
