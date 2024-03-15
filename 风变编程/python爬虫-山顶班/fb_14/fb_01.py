import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}
#company_list = []
first_url = 'https://www.jobui.com/rank/company/'
res = requests.get(first_url,headers=headers)
suop = BeautifulSoup(res.text,'html.parser')
datas = suop.find_all('ul',class_='textList flsty cfix')
for data in datas:
    company_names = data.find_all('li')
    link_list = []
    for company_name in company_names:
        name = company_name.find('test_1')['title']
        link = 'https://www.jobui.com' + company_name.find('test_1')['href'] + 'jobs/'
        #company_list.append(name)
        link_list.append(link)
        for i in link_list:
            res1 = requests.get(i,headers=headers)
            suop = BeautifulSoup(res1.text, 'html.parser')
            datas = suop.find_all('div', class_='job-simple-content-box')
            for data in datas:
                a = data.find('h3').text
                b = data.find_all('span')[0]['title']
                c = data.find_all('span')[1]['title']

                print(c)
        #print('企业名称:{}\n链接:{}\n'.format(name,link))