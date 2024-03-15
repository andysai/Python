# 导入模块
import requests
from bs4 import BeautifulSoup

url = 'https://y.qq.com/n/ryqq/playlist/7713574197'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}

# 获取网页数据
r = requests.get(url, headers=headers)

suop = BeautifulSoup(r.text, "lxml")
div_list = suop.find_all('span', class_='songlist__songname_txt')

for i in div_list:
    song_name = i.a.text

    print(song_name)
