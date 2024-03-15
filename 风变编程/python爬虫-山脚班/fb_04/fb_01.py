import requests
from bs4 import BeautifulSoup

URL = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=39981498405651123&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=2045061935&loginUin=344319484&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
res = requests.get(URL)
soup = res.json()
for key,values in soup.items():
    if key == 'data':
        for key,value in values.items():
            if key == 'song':
                for key,titles in value.items():
                    if key == 'list':
                        print(key,value)
                        for i in titles:
                            print(i['name'])
