import requests
from bs4 import BeautifulSoup
for i in range(3):
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.25Safari / 537.36Core / 1.70.3741.400QQBrowser / 10.5.3863.400'
    }
    url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(i + 1)
    res = requests.get(url)
    datas = BeautifulSoup(res.text,'html.parser').find('ul',class_='bang_list clearfix bang_list_mode').find_all('li')
    for data in datas:
        name = data.find('div',class_='name').text
        author = data.find('div',class_='publisher_info').text
        price = data.find('span',class_='price_n').text
        print('图书名:{}\n作者:{}\n价格{}\n'.format(name,author,price))
