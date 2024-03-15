import requests,random,smtplib,schedule,time
from bs4 import BeautifulSoup
from urllib.request import quote
from email.mime.text import MIMEText
from email.header import Header

# 获取电影名单
def get_movie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    movie_list = []
    for x in range(10):
        URL = 'https://movie.douban.com/top250?start=' + str(x) + '&filter='
        res_movie = requests.get(URL,headers=headers)
        suop_movies = BeautifulSoup(res_movie.text,'html.parser').find_all('div',class_='item')
        for suop_movie in suop_movies:
            movie_name = suop_movie.find(class_='title').text
            movie_list.append(movie_name)
    return movie_list

# 下载电影
def download_movie(movie_name):
    movie_name= movie_name
    gbk_movie = movie_name.encode('gbk')
    find_movie = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=' + quote(gbk_movie)
    res_movie = requests.get(find_movie)
    res_movie.encoding = 'gbk'
    suop_movies = BeautifulSoup(res_movie.text,'html.parser').find(class_='co_content8').find_all('table')
    if suop_movies:
        movie_link = 'https://www.ygdy8.com' + suop_movies[0].find('test_1')['href']
        res_movie1 = requests.get(movie_link)
        res_movie1.encoding = 'gbk'
        movie_download_link = BeautifulSoup(res_movie1.text,'html.parser').find('div',id='Zoom').find('span').find('table').find('test_1')['href']
        return movie_name + '的链接为:' + movie_download_link
    else:
        return '没有找到' + movie_name + '的链接'

# 通过随机数获取电影名称
def chooise_movie():
    l = []
    for i in range(3):
        x = random.randint(1,250)
        if x in l:
            continue
        else:
            l.append(x - 1)
    return l

# 获取电影名和下载链接
def main():
    movie_str = ''
    for i in chooise_movie():
        movie_name = get_movie()[i]
        movie_str += download_movie(movie_name)  + "\n"
    return movie_str

# 发送邮件
def send_mail():
    mailhost = 'smtp.casc.ac.cn'
    cascmail = smtplib.SMTP()
    cascmail.connect(mailhost,25)
    account = 'czl@casc.ac.cn'
    password = 'idc888888'
    cascmail.login(account, password)
    receiver = '344319484@qq.com'
    message = MIMEText(main(),'plain','utf-8')
    subject = '豆瓣高评分电影下载'
    message['Subject'] = Header(subject,'utf-8')
    try:
        cascmail.sendmail(account,receiver,message.as_string())
        return '邮件发送成功'
    except:
        return '邮件发送失败'
    cascmail.quit()

# 创建定时任务
def job():
    print('第一次发送')
    send_mail()
    time.sleep(2)
    print('发送成功')

# 定时任务执行时间
schedule.every(5).seconds.do(job)

# 每个定时任务执行间隔
while True:
    schedule.run_pending()
    time.sleep(2)