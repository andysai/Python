import requests,json

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
def login_in():
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data = {
        'log': 'spiderman',
        'pwd': 'crawler334566',
        'wp-submit': '登录',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': '1'
    }
    res_session = session.post(url,headers=headers,data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(login_in().cookies)
    cookies_str = json.dumps(cookies_dict)
    f = open('a.txt','w',encoding='utf-8')
    f.write(cookies_str)
    f.close()
    return res_session

def cookies_read():
    f = open('a.txt', 'r', encoding='utf-8')
    cookies_str = json.loads(f.read())
    f.close()
    cookies_dict = requests.utils.cookiejar_from_dict(cookies_str)
    return cookies_dict


def comment():
    message = input("请输入你要发表的评论内容:")
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data = {
        'comment': message,
        'submit': '发表评论',
        'comment_post_ID': '23',
        'comment_parent': '0'
    }
    comment = requests.post(url, headers=headers, data=data, cookies=cookies_read())
    return comment

try:
    session.cookies = cookies_read()
except FileNotFoundError:
    login_in()
    session.cookies = cookies_read()

num = comment()
if num.status_code == 200:
    print('成功啦！')
else:
    login_in()
    session.cookies = cookies_read()
    num = comment()