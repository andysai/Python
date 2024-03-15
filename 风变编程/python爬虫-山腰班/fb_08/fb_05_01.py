# 导入模块
import requests,json
# 创建会话
session = requests.session()
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
def cookies_read():
    cookies_txt = open('cookies.txt','r',encoding='utf-8')
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return cookies

def sign_in():
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data = {'log': 'spiderman',
            'pwd': 'crawler334566',
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
            'testcookie': '1'
            }
    session.post(url,headers=headers,data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    cookies_txt = open('cookies.txt', 'w', encoding='utf-8')
    cookies_txt.write(cookies_str)
    cookies_txt.close()

def send_message():
    url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_1 = {
        'comment': input('请输入你要发表的评论：'),
        'submit': '发表评论',
        'comment_post_ID': '13',
        'comment_parent': '0'
    }
    return requests.post(url_1,headers=headers,data=data_1)

try:
    session.cookies = cookies_read()
except FileNotFoundError:
    sign_in()
    session.cookies = cookies_read()
num = send_message()
if num.status_code == 200:
    print('成功啦！')
else:
    sign_in()
    session.cookies = cookies_read()
    num = send_message()