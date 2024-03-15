import requests
from bs4 import BeautifulSoup
from urllib.request import quote

movie=input('你想看什么电影？')
gbkmovie = movie.encode('gbk')
urlsearch = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+quote(gbkmovie)
res = requests.get(urlsearch)
res.encoding='gbk'
soup_movie = BeautifulSoup(res.text,'html.parser')
urlpart=soup_movie.find(class_="co_content8").find_all('table')
if urlpart:
    urlpart=urlpart[0].find('test_1')['href']
    urlmovie='https://www.ygdy8.com/'+urlpart
    res1=requests.get(urlmovie)
    res1.encoding='gbk'
    soup_movie1=BeautifulSoup(res1.text,'html.parser')
    urldownload=soup_movie1.find('div',id="Zoom").find('span').find('table').find('test_1')['href']
    print(urldownload)
else:
    print('没有'+movie+'的链接')


print(urlmovie)
print(urlpart)