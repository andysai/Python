import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_foods = bs_foods.find_all('div',class_='info pure-u')
# 查找最小父级标签

tag_a = list_foods[0].find('test_1')
# 提取第0个父级标签中的<test_1>标签
name = tag_a.text[17:-13]
# 菜名，使用[17:-13]切掉了多余的信息
URL = 'http://www.xiachufang.com'+tag_a['href']
# 获取URL
tag_b = bs_foods.find('p',class_='ing ellipsis')
print(tag_b.text)
print(list_foods[0])