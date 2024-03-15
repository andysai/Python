import requests
music = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
res = music.content
with open('test.mp3','wb') as f:
    f.write(res)