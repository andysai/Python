from gevent import monkey
monkey.patch_all()
import time,requests,gevent

start = time.time()

url_lists = [
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'http://www.sohu.com/',
    'https://www.qq.com/',
    'https://www.163.com/',
    'http://www.iqiyi.com/',
    'https://www.tmall.com/',
    'http://www.ifeng.com/'
    ]

def crawler(url):
    r = requests.get(url)
    print(url,time.time()-start,r.status_code)

take_list = []

for url in url_lists:
    task = gevent.spawn(crawler,url)
    take_list.append(task)
gevent.joinall(take_list)
end = time.time()
print(end-start)
