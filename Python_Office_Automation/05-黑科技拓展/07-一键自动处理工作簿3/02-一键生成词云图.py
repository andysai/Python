# -*- coding: utf-8 -*-
import os
import time
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba

# 分词
def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result


# 获取指定后缀的文件
def get_filename(path):  # 输入路径、文件类型 例如'.csv'
    file_name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            file_name.append(i)
    return file_name  # 输出由有后缀的文件名组成的列表

# 生成词云
def word_cloud(img_file_list, text_file_list, text_path, img_path):
    # 读取文档
    for file_name in text_file_list:
        file = open(text_path + "/" + file_name, "r")
        str_file = file.read()
        file.close()

        str_text = trans_CN(str_file)
        mask = np.array(image.open(img_path + "/" + img_file_list[text_file_list.index(file_name) % 4]))

        # 1.添加遮罩层;2.# 生成中文字的字体,必须要加,不然看不到中文
        wordcloud = WordCloud(mask=mask, font_path="C:\Windows\Fonts\STXINGKA.TTF").generate(str_text)
        image_produce = wordcloud.to_image()
        print("正在生成...")
        # image_produce.show()

        # 保存词云文件
        img_wc_path = "../source_material/07/02一键生成词云图/词云图片"
        isExists = os.path.exists(img_wc_path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(img_wc_path)
        else:
            pass
        image_produce.save(img_wc_path + "/" + file_name[:-4] + ".jpg")
        print("词云图片已保存...")
        time.sleep(0.4)

# 程序执行入口
if __name__ == '__main__':
    text_path = "../source_material/07/02一键生成词云图/词云文本"

    img_path = "../source_material/07/02一键生成词云图/词云参照图形"

    # 获取所有的文件
    text_file_list = get_filename(text_path)
    # print(img_file_list)

    # 获取所有的图像文件
    img_file_list = get_filename(img_path)
    print(img_file_list)

    # 批量生成词云
    word_cloud(img_file_list, text_file_list, text_path, img_path)
