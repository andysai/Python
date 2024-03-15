import requests
# 引入BS库
from bs4 import BeautifulSoup

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
print(soup)