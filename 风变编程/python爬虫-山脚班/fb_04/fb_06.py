from pyquery import PyQuery as pq
doc = pq('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=49036620903919751&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E4%BB%93%E6%9C%A8%E9%BA%BB%E8%A1%A3&g_tk=2079542702&loginUin=344319484&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# doc1 = pq(url='https://www.baidu.com')
print(doc)
print(doc('head'))