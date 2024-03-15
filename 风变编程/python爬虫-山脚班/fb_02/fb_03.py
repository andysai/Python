import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
test = res.text
html = BeautifulSoup(test,'html.parser')
# mess = html.find_all('div',class_='comment-author vcard"') # 获取评论人的名字
mess1 = html.find_all('div',class_='comment-content')
for mes in mess1:
    message = mes.find('p')
    print(message.text)