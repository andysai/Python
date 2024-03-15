import requests

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?'
for i in range(5):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
    }
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.center',
        'searchid': '39853066037619909',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(i+1),
        'n': '10',
        'w': '仓木麻衣',
        'g_tk': '210864166',
        'loginUin': '344319484',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'}

    res_music = requests.get(url,headers=headers,params=params)
    json_music = res_music.json()
    get_musics = json_music['data']['song']['list']
    for get_music in get_musics:
        name = get_music['name']
        album = get_music['album']['name']
        time = str(get_music['interval']) + '秒'
        link = 'https://y.qq.com/n/yqq/song/' + get_music['mid'] + '.html'
        print('歌曲名:{}\n专辑为:{}\n播放时长:{}\n链接:{}\n'.format(name,album,time,link))