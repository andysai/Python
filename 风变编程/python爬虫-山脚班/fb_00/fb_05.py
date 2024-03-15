import requests
res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
photo = res.content
with open('test.jpg','wb') as f:
    f.write(photo)