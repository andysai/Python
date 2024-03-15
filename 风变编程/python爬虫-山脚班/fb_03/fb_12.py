import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开

for x in range(100):
    table_number = str(x*44)
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 标记了请求从什么设备，什么浏览器上发出
        }
    # commodity = input('你想查什么商品？')
    commodity = '猫砂'
    commodity = commodity.encode('gbk')
    URL ='https://s.taobao.com/'
    # new_url = URL + '/search?initiative_id=staobaoz_20191127&q=' + quote(commodity) + '&bcoffset=-9&ntoffset=-9&p4ppushleft=1%2C48&s=' + table_number
    # print(new_url)
    new_url = 'https://s.taobao.com//search?initiative_id=staobaoz_20191127&q=%E7%8C%AB%E7%A0%82&bcoffset=-9&ntoffset=-9&p4ppushleft=1%2C48&s=2112'
    get_url = requests.get(new_url,headers=headers)
    suop = BeautifulSoup(get_url.content,'html.parser')
    web_find = suop.find_all('div', class_="item J_MouserOnverReq  ")

print(suop)
