import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}
for i in range(2):
    url1 = 'https://book.douban.com/top250?start=' + str(i * 25)
    res = requests.get(url1,headers=headers)
    suop = BeautifulSoup(res.text,'html.parser')
    datas = suop.find_all('tr',class_='item')
    for data in datas:
        book_name = data.find_all('test_1')[1]['title']
        book_link = data.find_all('test_1')[1]['href'] + 'comments/hot?p=1'
        res1 = requests.get(book_link,headers=headers)
        suop1 = BeautifulSoup(res1.text,'html.parser')
        datas = suop1.find_all('div',id='content')
        for data in datas:
            name = data.find('h1').text[:-3]
            #comment_IDcomment_ID = data.find_all('test_1')[0]['title']
            #Short_commentary_content = data.find('span',class_='short').text.strip()
            #print('书名:{}\n评论ID:{}\n短评内容:{}\n'.format(book_name,comment_IDcomment_ID,Short_commentary_content))
            print(name)