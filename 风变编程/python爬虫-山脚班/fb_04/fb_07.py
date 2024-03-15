import requests
import json

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

URL = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery1124024536718764915166_1574989152108&keyword=%E4%BB%93%E6%9C%A8%E9%BA%BB%E8%A1%A3&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1574989152116'
res_music = requests.get(URL, headers=headers)
json_music = res_music.content.decode().replace(')', '').replace(
            'jQuery1124024536718764915166_157498915210(', '')
views = json.loads(json_music)
print(json_music)
