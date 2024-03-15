# 导入库
import os
from docx import Document
import time
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba
import random

# 分词
def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result

# 获取所有的路径信息
def get_filepth(path, filetype):
    for root, dirs, files in os.walk(path):
        return files

# 生成词云
def word_cloud(img_file_list, file_name, path_list):
    n = 0
    for file_single in file_name:
        # 循环加载原有文档
        document = Document(path_list[0] + "/" + file_single)

        str_word = ""
        for p in document.paragraphs:
            str_word += p.text
        str_text = trans_CN(str_word)
        # ------生成词云
        mask = np.array(image.open(path_list[1] + "/" + img_file_list[random.randint(0, 4)]))

        # 添加遮罩层 生成中文字的字体，必须要加，不然看不到中文
        wordcloud = WordCloud(mask=mask, font_path="C:/Windows/Fonts/STXINGKA.TTF").generate(str_text)
        image_produce = wordcloud.to_image()
        print("正在生成...")
        image_produce.show()

        # ------
        # 保存词云文件
        isExists = os.path.exists(path_list[2])
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs("../source_material/04/04一键根据文档生成词云图/词云图片")
        else:
            pass

        image_produce.save(path_list[2] + "/" + str(n) + ".jpg")
        n += 1
        print("词云图片已保存...")
        time.sleep(0.4)
        # ------

# 程序执行入口
if __name__ == '__main__':
    # 先获取所有的路径信息
    path1 = "../source_material/04/04一键根据文档生成词云图/词云文本"
    path2 = "../source_material/04/04一键根据文档生成词云图/词云参照图形"
    path3 = "../source_material/04/04一键根据文档生成词云图/词云图片"
    # 获取所有docx文件
    file_name = get_filepth(path1, ".docx")
    print(file_name)

    # 获取所有图像文件
    img_file_list = get_filepth(path2, ".jpg")
    print(img_file_list)

    path_list = [path1, path2, path3]
    # 生成词云
    word_cloud(img_file_list, file_name, path_list)
