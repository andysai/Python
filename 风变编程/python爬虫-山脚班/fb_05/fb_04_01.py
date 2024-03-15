# 导入模块
import requests

url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?'

for i in range(5):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    params = {
        'g_tk': '210864166',
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
        'topid': '102065756',
        'cmd': '8',
        'needmusiccrit': '0',
        'pagenum': str(i),
        'pagesize': '25',
        'lasthotcommentid': 'song_102065756_656300800_1575128321',
        'domain': 'qq.com',
        'ct': '24',
        'cv': '10101010'
    }
    music_res = requests.get(url,headers=headers,params=params)
    music_json = music_res.json()
    music_lists = music_json['comment']['commentlist']
    for list in music_lists:
        print(list['rootcommentcontent'])
        print('-----------------')
