get_headers = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh,zh-CN;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5
Cache-Control: max-age=0
Connection: keep-alive
Cookie: td_cookie=1454423945; yd_cookie=2b904a64-17ad-4f16bcd459e1d28615a0aea7761192fce765; _ydclearance=9033ef9848b250e247ced589-1ff4-4201-8406-0c3003eddab6-1575945942; _userCode_=20191210845432805; _userIdentity_=20191210845437327; _tt_=F6956E8BA0C31BA19FEACD8190F0D210; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1575938743; DefaultCity-CookieKey=3462; DefaultDistrict-CookieKey=0; __utma=196937584.928538004.1575938743.1575938743.1575938743.1; __utmc=196937584; __utmz=196937584.1575938743.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _movies_=15167; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1575940578
Host: www.mtime.com
Referer: http://www.mtime.com/top/tv/top100/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'''
headers = dict([line.split(": ",1) for line in get_headers.split("\n")])

import requests,csv,gevent
from bs4 import BeautifulSoup

url = 'http://www.mtime.com/top/tv/top100/'
res = requests.get(url,headers=headers)
print(res.status_code)
bs_res = BeautifulSoup(res.text,'html.parser').find_all('div',class_='mov_con')
for i in bs_res:
    #TV_name = i.find('h2').text
    #print('\n剧名:{}'.format(TV_name))
    TV_data = ''
    TV_message = i.find_all('p')
    for data in TV_message:
        TV_data = TV_data + ' ' + data.text
    print(TV_data)

    #print(director.text)
    #print(To_star.text)
