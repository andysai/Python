import requests
import json

url = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112403109777398223168_1623825726797&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1623825726799'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}

r = requests.get(url, headers=headers)

json_string = r.text

json_string = json_string[json_string.find('{'): -2]
json_data = json.loads(json_string)
comment_list = json_data['results']['parents']
for eachone in comment_list:
    message = eachone['content']
    print(message)

