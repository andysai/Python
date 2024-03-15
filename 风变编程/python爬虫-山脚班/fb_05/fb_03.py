import requests
import json

URL = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers = {
    'referer': 'https://y.qq.com/portal/search.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

for i in range(5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.center',
        'searchid': '38547116784331445',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(i + 1),
        'n': '10',
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
    res_music = requests.get(URL,params=params)
    json_music = json.loads(res_music.text)
    list_music = json_music['data']['song']['list']
    for music in list_music:
        name = music['name']
        album = music['album']['name']
        time = str(music['interval']) + '秒'
        link = 'https://y.qq.com/n/yqq/song/' + music['mid'] + '.html'
        print('歌曲名:{}\n专辑名:{}\n播放时长:{}\n播放链接:{}\n'.format(name, album, time, link))