#  序号/电影名/评分/推荐语/链接
import requests,random
from bs4 import BeautifulSoup
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title='movies'
sheet['A1'] = '序号'
sheet['B1'] = '电影名'
sheet['C1'] = '评分'
sheet['D1'] = '推荐语'
sheet['E1'] = '链接'
a_list = []
for x in range(10):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 标记了请求从什么设备，什么浏览器上发出
    }
    URL = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    # URL = 'https://movie.douban.com/top250?start=0&filter='
    res = requests.get(URL,headers=headers)
    suop = BeautifulSoup(res.text,'html.parser')
    web = suop.find('ol',class_='grid_view')
    for mes in web.find_all('li'):
        movie_number = mes.find('em',class_="")
        movie_name = mes.find('span',class_='title')
        movie_score = mes.find('span',class_='rating_num')
        movie_Rl = mes.find('span',class_='inq')
        movie_link = mes.find('test_1')
        if movie_Rl == None:
            #print('序号:{}\n电影名:{}\n评分:{}\n推荐语:{}\n链接:{}\n'.format(movie_number.text,movie_name.text,movie_score.text,'',movie_link['href']))
            a_list.append([movie_number.text, movie_name.text, movie_score.text, '', movie_link['href']])
        else:
            #print('序号:{}\n电影名:{}\n评分:{}\n推荐语:{}\n链接:{}\n'.format(movie_number.text, movie_name.text, movie_score.text,movie_Rl.text, movie_link['href']))
            a_list.append([movie_number.text, movie_name.text, movie_score.text, movie_Rl.text, movie_link['href']])
for i in a_list:
    sheet.append(i)
print(a_list)
wb.save('movies.xlsx')