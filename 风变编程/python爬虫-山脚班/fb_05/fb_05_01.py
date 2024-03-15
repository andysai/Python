import requests

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers = {
    'referer': 'https://y.qq.com/portal/search.html',
    # 请求来源
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 标记了请求从什么设备，什么浏览器上发出
    }
for i in range(5):
    params = {'ct': '24',
            'qqmusic_ver': '1298',
            'remoteplace': 'txt.yqq.lyric',
            'searchid': '97691303219932754',
            'aggr': '0',
            'catZhida': '1',
            'lossless': '0',
            'sem': '1',
            't': '7',
            'p': str(i + 1),
            'n': '5',
            'w': '仓木麻衣',
            'g_tk': '945899764',
            'loginUin': '344319484',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
              }
    res_lyric = requests.get(url,headers=headers,params=params)
    res_json = res_lyric.json()
    lyric_lists = res_json['data']['lyric']['list']
    for lyric_list in lyric_lists:
        name = lyric_list['albumname']
        lyric = lyric_list['content']
        print('歌曲名:{}\n歌词:{}\n'.format(name,lyric))
        print('------------------------------')