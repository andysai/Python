import requests

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 标记了请求从什么设备，什么浏览器上发出
    }

URL = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=49036620903919751&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E4%BB%93%E6%9C%A8%E9%BA%BB%E8%A1%A3&g_tk=2079542702&loginUin=344319484&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
res_music = requests.get(URL)
josn_music = res_music.json()
get_music = josn_music['data']['song']['list']
for music in get_music:
    name = music['name']
    album = music['album']['name']
    time = str(music['interval']) + '秒'
    link = 'https://y.qq.com/n/yqq/song/' + music['mid'] + '.html'
    print('歌曲名:{}\n专辑名:{}\n播放时长:{}\n播放链接:{}\n'.format(name, album, time, link))
