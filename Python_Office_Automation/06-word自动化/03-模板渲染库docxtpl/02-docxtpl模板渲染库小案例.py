# 导入模块
from docxtpl import DocxTemplate

data_dic = {'t1': '花针', 't2': '牛毛', 't3': '细丝', 't4': '春姑娘', 't5': '春雨贵如油', 't6': '竟相开放', 't7': '美伦美奂', 't8': '含苞欲放'}

# 加载模板文件
document = DocxTemplate("../source_material/03/A/春天来了_模板.docx")
document.render(data_dic)
document.save("../source_material/03/A/春天来了_修改后.docx")
