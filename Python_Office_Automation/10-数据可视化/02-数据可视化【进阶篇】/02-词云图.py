import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
#r''单引号里面不需要转义
path = '../source_material/02/images'
font = r'C:\Windows\Fonts\SIMKAI.TTF'#电脑自带的字体
def tcg(texts):
    cut = jieba.cut(texts)  #分词
    string = ' '.join(cut)
    return string
text = (open(path+r'./cloud.txt','r',encoding='utf-8')).read()
string=tcg(text)
img = Image.open(path+r'./1.png') #打开图片
img_array = np.array(img) #将图片装换为数组
stopword=['']  #设置停止词，也就是你不想显示的词
wc = WordCloud(
    background_color='white',
    width=1000,
    height=800,
    mask=img_array, #设置背景图片
    font_path=font,
    stopwords=stopword
)
wc.generate_from_text(string)#绘制图片
plt.imshow(wc)
plt.axis('off')
plt.show()  #显示图片
wc.to_file('../source_material/02/02-词云图.png')  #保存图片
