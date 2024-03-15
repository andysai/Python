import requests
import json

URL = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers = {
    'referer': 'https://y.qq.com/portal/search.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

for i in range(5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'remoteplace': 'txt.yqq.lyric',
        'searchid': '91990683340084024',
        'aggr': '0',
        'catZhida': '1',
        'lossless': '0',
        'sem': '1',
        't': '7',
        'p': str(i + 1),
        'n': '5',
        'w': '周杰伦',
        'g_tk': '347902107',
        'loginUin': '344319484',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }

    res_music = requests.get(url,params=params)
    json_music = json.loads(res_music.text)
    list_music = json_music['data']['lyric']['list']
    for music in list_music:
        print(music['content'])