import requests
from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='http://www.weather.com.cn/weather/101280601.shtml'
res=requests.get(url,headers=headers)
res.encoding = 'utf-8'
res_find = BeautifulSoup(res.text,'html.parser').find('ul',class_='t clearfix')
data = res_find.find('h1')
weather = res_find.find(class_='wea')
max_air_temperature = res_find.find('span')
min_max_air_temperature = res_find.find('i')
wea = '日期:{}\n天气:{}\n温度{}℃/{}'.format(data.text,weather.text,max_air_temperature.text,min_max_air_temperature.text)
