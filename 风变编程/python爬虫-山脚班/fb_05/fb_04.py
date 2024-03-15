import requests

URL = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
for i in range(5):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
    }
    params = {
        'g_tk': '2079542702',
        'loginUin': '344319484',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'GB2312',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        'cid': '205360772',
        'reqtype': '2',
        'biztype': '1',
        'topid': '97773',
        'cmd': '8',
        'needmusiccrit': '0',
        'pagenum': str(i),
        'pagesize': '25',
        'lasthotcommentid': '',
        'domain': 'qq.com',
        'ct': '24',
        'cv': '10101010'
    }
    res_music = requests.get(URL, params=params, headers=headers)
    json_music = res_music.json()
    list_music = json_music['comment']['commentlist']
    for comment in list_music:
        print(comment['rootcommentcontent'])
        print('-----------------------------------')