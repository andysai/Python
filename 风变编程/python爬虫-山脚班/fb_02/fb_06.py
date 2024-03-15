import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
web = res.text
test = BeautifulSoup(web,'html.parser')
html = test.find_all('header',class_='entry-header')
# print(html)
for i in html:
    time = i.find('time')
    link = i.find('test_1')
    name = i.find('h2',class_='entry-title')
    print('文章标题:{}\n发布时间:{}\n文章链接:{}\n'.format(name.text,time.text,link['href']))