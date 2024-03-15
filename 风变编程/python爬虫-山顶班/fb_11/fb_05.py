# 项目目标：使用多协程和队列，爬取时光网电视剧TOP100的数据（剧名、导演、主演和简介），并用csv模块将数据存储下来。
# 时光网TOP100链接：http://www.mtime.com/top/tv/top100/
#提示：
#1.分析数据存在哪里（打开“检查”工具，刷新页面，查看第0个请求，看【response】）
#2.观察网址规律（多翻几页，看看网址会有什么变化）
#3.获取、解析和提取数据（需涉及知识点：queue、gevent、request、BeautifulSoup、find和find_all）
#4.存储数据（csv本身的编码格式是utf-8，可以往open（）里传入参数encoding='utf-8'。这样能避免由编码问题引起的报错。)
#注：在练习的【文件】中，你能找到自己创建的csv文件。将其下载到本地电脑后，请用记事本打开，因为用Excel打开可能会因编码问题出现乱码。

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

from gevent import monkey
monkey.patch_all()
import requests,time,csv,gevent
from bs4 import BeautifulSoup
from gevent.queue import Queue

# 添加TOP100电视剧的链接
url_lists = []
for i in range(1,11):
    if i == 1:
        url = 'http://www.mtime.com/top/tv/top100/'
        url_lists.append(url)
    else:
        url = 'http://www.mtime.com/top/tv/top100/index-' + str(i) + '.html'
        url_lists.append(url)
work = Queue()
for url_list in url_lists:
    work.put_nowait(url_list)
def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url_list,headers=headers)
        bs_res = BeautifulSoup(res.text, 'html.parser').find_all('div', class_='mov_con')
        for i in bs_res:
            TV_name = i.find('h2').text
            TV_data = ''
            TV_message = i.find_all('p')
            for data in TV_message:
                TV_data = TV_data + ' ' + data.text
            writer.writerow([TV_name,TV_data])
            return [TV_name,TV_data]

f = open('movie.xlsx','w',newline='',encoding='utf-8')
writer = csv.writer(f)
tasks_list = []

for x in range(8):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)
print(crawler())