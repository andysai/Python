# URL http://books.toscrape.com/
import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/')
html = res.text
message = BeautifulSoup(html,'html.parser')
mess = message.find_all('div',class_='side_categories')
for mes in mess:
    #print(mes)
    mes1 = mes.find('li')
    print(mes1.text)