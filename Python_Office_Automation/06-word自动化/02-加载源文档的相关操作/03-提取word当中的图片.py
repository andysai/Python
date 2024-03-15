from docx import Document
from docx2python import docx2python

# 加载原有文档，绝对或者相对路径都可以
document = docx2python("../source_material/02/A/python简介.docx")

# print(dir(document.images))

for key, value in document.images.items():
    f = open("../source_material/02/A/images/" + key, "wb")
    f.write(value)
    f.close()
