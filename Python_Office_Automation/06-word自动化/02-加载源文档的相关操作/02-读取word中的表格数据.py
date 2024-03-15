from docx import Document


# 加载原有文档，绝对或者相对路径都可以
document = Document("../source_material/02/A/python简介.docx")

# print(dir(document))

for table in document.tables:
    rows_value = len(table.rows)
    for i in range(rows_value):
        for cell in table.row_cells(i):
            print(cell.text)
            print("----------")
