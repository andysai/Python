import requests
from bs4 import BeautifulSoup
link1 = 'http://www.xiachufang.com'
res = requests.get('http://www.xiachufang.com/explore/')
html = res.text
suop = BeautifulSoup(html,'html.parser')
web = suop.find_all('div',class_='info pure-u')
#print(web)
list_all = []
for i in web:
    name = i.find(target='_blank')
    link = i.find('p',class_='ing ellipsis')
    list_all.append([name.text.strip(),link.text.strip(),link1+name['href']])
    #print('菜名为:{}\n需要的材料:{}\n做法链接:{}\n'.format(name.text.strip(),link.text.strip(),link1+name['href']))
print(list_all)