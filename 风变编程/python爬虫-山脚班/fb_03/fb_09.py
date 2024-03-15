#  序号/电影名/评分/推荐语/链接
import requests,random
from bs4 import BeautifulSoup
import re

for x in range(10):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 标记了请求从什么设备，什么浏览器上发出
    }
    URL = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    # URL = 'https://movie.douban.com/top250?start=0&filter='
    res = requests.get(URL,headers=headers)
    suop = BeautifulSoup(res.text,'html.parser')
    web = suop.find('ol',class_='grid_view')
    for mes in web.find_all('li'):
        movie_number = mes.find('em',class_="")
        movie_name = mes.find('span',class_='title')
        movie_score = mes.find('span',class_='rating_num')
        movie_Rl = mes.find('span',class_='inq')
        movie_year = mes.find('p',class_="")
        movie_link = mes.find('test_1')
        l = len(movie_year.text)

        numbers = []

        i = 0
        while i < l:
            num = ''
            symbol = movie_year.text[i]
            while '0' <= symbol <= '9':  # symbol.isdigit()
                num += symbol
                i += 1
                if i < l:
                    symbol = movie_year.text[i]
                else:
                    break
            i += 1
            if num != '':
                numbers.append(int(num))
                print(numbers)