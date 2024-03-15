import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
novel = res.text
story = open('story.txt','w',encoding='utf-8')
story.write(novel)
story.close()
# print(novel[:800])
