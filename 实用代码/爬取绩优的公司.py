import requests
from bs4 import BeautifulSoup

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
url = "http://www.iwencai.com/unifiedwap/result?w=2020%E5%B9%B4%E5%87%80%E5%88%A9%E6%B6%A6%E5%90%8C%E6%AF%94%E5%A2%9E%E9%95%BF20%25%E4%BB%A5%E4%B8%8A%EF%BC%8C2021%E5%B9%B4%E4%B8%AD%E6%8A%A5%E5%87%80%E5%88%A9%E6%B6%A6%E5%90%8C%E6%AF%94%E5%A2%9E%E9%95%BF60%25%E4%BB%A5%E4%B8%8A%EF%BC%8C120%E6%97%A5%E5%9D%87%E7%BA%BF250%E5%9D%87%E7%BA%BF%E6%96%B9%E5%90%91%E5%90%91%E4%B8%8A%EF%BC%8C%E6%80%BB%E5%B8%82%E5%80%BC%E5%A4%A7%E4%BA%8E70%E4%BA%BF%E5%85%83&querytype=&issugs"
res = requests.get(url, headers=headers)
bstitle = BeautifulSoup(res.text, 'html.parser')
s = bstitle.find_all('tr')
print(bstitle)


