# http://books.toscrape.com/catalogue/category/books/travel_2/index.html
import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
html = res.text
status = res.status_code # 测试网站是否正常
a = BeautifulSoup(html,'html.parser')
test = a.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for i in test:
    name = i.find('h3')
    stat = i.find('p')
    price = i.find('p',class_='price_color')
    print('书本:{},评分:{},价格:{}'.format(name.text,stat['class'][1],price.text))