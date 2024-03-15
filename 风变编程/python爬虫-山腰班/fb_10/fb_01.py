import time
from selenium import webdriver
from bs4 import BeautifulSoup

#Chrome_Options = webdriver.ChromeOptions()
#Chrome_Options.add_argument('headless')
#driver = webdriver.Chrome(options = Chrome_Options)
driver = webdriver.Chrome()
driver.get('http://www.weather.com.cn/weather/101280601.shtml')
time.sleep(2)
page_source = driver.page_source
res_find = BeautifulSoup(page_source,'html.parser').find('ul',class_='t clearfix')
data = res_find.find('h1')
weather = res_find.find(class_='wea')
max_air_temperature = res_find.find('span')
min_max_air_temperature = res_find.find('i')
print('日期:{}\n天气:{}\n温度{}℃/{}'.format(data.text,weather.text,max_air_temperature.text,min_max_air_temperature.text))
driver.close()