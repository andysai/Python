import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

for i in range(3):
    url = 'https://book.douban.com/top250?start=' + str( i * 25 )
    res = requests.get(url,headers=headers)
    suops = BeautifulSoup(res.text,'html.parser').find_all('td',valign='top')
    for suop in suops:
        name = suop.find('test_1').text.strip()
        message = suop.find('p')
        print(name)