# 导入模块
import requests
from bs4 import BeautifulSoup

def get_movies():
    # 定制请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
        'Host': 'movie.douban.com'}

    # 创建空列表
    movie_list = []
    for i in range(0, 10):
        # 获取网址
        url = 'https://movie.douban.com/top250?start=' + str(i*25)

        # 获取网页数据
        r = requests.get(url, headers=headers)

        suop = BeautifulSoup(r.text, "lxml")
        div_list = suop.find_all('div', class_='hd')
        for each in div_list:
            movie_name = each.a.span.text.strip()
            movie_director = each.p.text.strip()
            movie_list.append(movie_name, movie_director)
        return movie_list

movies = get_movies()
print(movies)
