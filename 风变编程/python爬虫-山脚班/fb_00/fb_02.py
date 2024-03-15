import requests
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
pic = res.content
photo = open('ppt.jpg','wb')
photo.write(pic)
photo.close()