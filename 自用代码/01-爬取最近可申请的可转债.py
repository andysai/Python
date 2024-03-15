import requests
from bs4 import BeautifulSoup

url = 'http://data.eastmoney.com/kzz/default.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.51 Safari/537.36 Edg/92.0.902.15',
           'Host': 'data.eastmoney.com'}

r = requests.get(url, headers=headers)

suop = BeautifulSoup(r.text, 'lxml')

div_list = suop.find_all('table', style_='display: table;')

for i in div_list:
    a = i
    print(a)
