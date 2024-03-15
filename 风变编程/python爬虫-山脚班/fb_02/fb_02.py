import requests
from bs4 import BeautifulSoup

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html = res.text
suop = BeautifulSoup(html,'html.parser')
mess = suop.find_all('div',class_='books')
for mes in mess:
    kind = mes.find('h2')
    title = mes.find(class_='title')
    brief = mes.find(class_='info')
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text,'\n')