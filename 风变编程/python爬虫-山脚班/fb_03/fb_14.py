import requests
from bs4 import BeautifulSoup

url = 'http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/e/'
res = requests.get(url)
suop = BeautifulSoup(res.text,'html.parser')
titles = suop.find('pre')
for title in titles.find_all('test_1'):
    name = title.text
    name_list = ['Name','modified','Size','Description','Parent Directory','Last modified']
    link = title['href']
    if name in name_list:
        pass
    else:
        print('包名为:{}\n下载地址为:{}\n'.format(name,'http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/e/' + link))