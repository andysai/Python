import requests
from bs4 import BeautifulSoup

url = 'https://wenku.baidu.com/view/28d8e8e6f4335a8102d276a20029bd64793e6229.html'
res = requests.get(url)
res.encoding='gbk'
# print(res.status_code)
suop = BeautifulSoup(res.text,'html.parser')
print(suop)