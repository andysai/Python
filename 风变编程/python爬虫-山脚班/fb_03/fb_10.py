import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 标记了请求从什么设备，什么浏览器上发出
    }
URL_header = 'https://www.ygdy8.com'
movie_name = '无名之辈'
gbk_movie = movie_name.encode('gbk')
URL = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=' + quote(gbk_movie)

res = requests.get(URL)
# res.encoding = 'gbk'
suop = BeautifulSoup(res.text,'html.parser')
html = suop.find_all('div',class_='co_content8')
if html:
    for web in html:
        open_web = web.find('test_1')
        URL = URL_header + open_web['href']
        res = requests.get(URL,headers=headers)
        res.encoding = 'gbk'
        suop = BeautifulSoup(res.text, 'html.parser')
        html = suop.find('div',id='Zoom').find('span').find('table').find('test_1')['href']
        print(html)
else:
    print('没有' + movie_name)
