import requests
from bs4 import BeautifulSoup

for i in range(3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
    }

    url = 'https://book.douban.com/top250?start=' + str(i * 25)
    res = requests.get(url,headers=headers)
    datas = BeautifulSoup(res.text,'html.parser').find_all('tr',class_="item")
    for data in datas:
        title = data.find_all('test_1')[1]['title']
        publish = data.find('p',class_='pl').text
        score = data.find('span',class_='rating_nums').text
        print('书籍名称:{}\n出版信息:{}\n评分:{}\n'.format(title,publish,score))