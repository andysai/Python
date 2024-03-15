# 导入模块
import requests
# 网站访问URL
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

res = requests.post(url,headers=headers,data=data)
login_in = str(res.status_code)
if login_in == '200':
    print('登陆成功')
    cookies = res.cookies
    message = input("请输入你要发表的评论内容:")
    url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_1 = {
        'comment': message,
        'submit': '发表评论',
        'comment_post_ID': '23',
        'comment_parent': '0'
        }
    comment = requests.post(url_1,headers=headers,data=data_1,cookies=cookies)
    login_in_1 = str(comment.status_code)
    if login_in_1 == '200':
        print('发布成功')
    else:
        print('发布失败')
else:
    print('登陆失败')