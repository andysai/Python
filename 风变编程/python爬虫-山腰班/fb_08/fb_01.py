# 引入requests
import requests
# 把登录的网址赋值给url
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# 加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# 把有关登录的参数封装成字典，赋值给data
data = {
'log': 'spiderman',  #写入账户
'pwd': 'crawler334566',  #写入密码
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
'testcookie': '1'
}
# 用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in
login_in = requests.get(url,headers=headers,data=data)
# 打印login_in
print(login_in)

url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_1 = {
    'comment': '测试2222221111111111111111111111111111111111111111111111111111111111111111111111111',
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
send_message = requests.get(url_1,headers=headers,data=data_1)
print(send_message.status_code)