import requests
web = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
dayin = web.content
with open('index.html','wb') as f:
    f.write(dayin)