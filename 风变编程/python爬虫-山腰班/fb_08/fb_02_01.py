import requests,json

seesion = requests.session()
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# 增加请求头
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

# 用户登陆的请求信息
data = {
    'log': 'spiderman',
    'pwd': 'crawler334566',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}
res_seesion = seesion.post(url,headers=headers,data=data)

cookies_dict = requests.utils.dict_from_cookiejar(res_seesion.cookies)
print(cookies_dict)
cookies_str = json.dumps(cookies_dict)
print(cookies_str)
f = open('test_1,txt','w',encoding='utf=8')
f.write(cookies_str)
f.close()
print('--------------------------------------')
f = open('test_1,txt','r',encoding='utf=8')
message = f.read()
print(message)
cookies_str = json.loads(message)
print(cookies_str)
cookies_dict = requests.utils.cookiejar_from_dict(cookies_str)
print(cookies_dict)
seesion.cookies = cookies_dict
print(seesion)
f.close()