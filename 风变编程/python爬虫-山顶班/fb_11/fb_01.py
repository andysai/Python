import requests,time

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
for url in url_lists:
    res = requests.get(url)
    print(url,res.status_code)
end = time.time()
print(end-start)
