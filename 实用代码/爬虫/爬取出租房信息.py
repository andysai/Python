import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}
url = 'https://dg.anjuke.com/sale/fengganga-q-dgslcz/?from=SearchBar'

response = requests.get(url, headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
result_li = soup.find('section', {'class': 'list'})
print(result_li)
