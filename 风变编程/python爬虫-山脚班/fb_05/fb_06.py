# 请求参数转换
headers = '''Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: csrftoken=ugyL-K9H76ZEGyISYDi5YtgIp9TpD0xZOI4a0CS1mEg; WWWID=WWW21A0B2C6E402691952E72F8BAA8EF86F; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1575010586; TOKEN=DewpDSy6Ubd_-W_poYAm3MzjEOXXmRHBWOr-lvo33K8; loginId=266566718; loginName=13686635733; nickname=13686635733; loginEmail=null; loginMobile=13686635733; loginExt=null; loginSession=1; auth=1; loginType=SELLER; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1575011622
Host: www.kuaidi100.com
Referer: https://www.kuaidi100.com/
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400
X-Requested-With: XMLHttpRequest'''

headers = dict([line.split(": ",1) for line in headers.split("\n")])
print(headers)

from selenium import webdriver

driver = webdriver.PhantomJS()
url = "https://et.xiamenair.com/xiamenair/book/findFlights.action?lang=zh&tripType=0&queryFlightInfo=XMN,PEK,2018-01-15"
driver.get(url)
cookie_dict = []
# 获取cookie列表
cookie_list = driver.get_cookies()
# 格式化打印cookie
for cookie in cookie_list:
    cookie_dict[cookie['name']] = cookie['value']
print(cookie_dict)