# 导入模块
import requests
from bs4 import BeautifulSoup

# 定义link为网站地址
link = "http://www.santostang.com/"

# 定义请求头的浏览器代理，伪装成浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/88.0.4324.182 '
                         'Safari/537.36 '
                         'Edg/88.0.705.74'}

# 请求网页
r = requests.get(link, headers=headers)

# 使用BeautifulSoup解析
suop = BeautifulSoup(r.text, "html.parser")

# 找到第一篇文章标题,提取a里面的字符串，并进行空格去除
title = suop.find("h1", class_="post-title").a.text.strip()

# 打印内容
print(title)

# 创建一个空白的txt文件，然后使用f.write写入刚刚的字符串title
with open('03-存储数据.txt', 'w') as f:
    f.write(title)
    f.close()
