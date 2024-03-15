# 请求参数转换
headers = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh,zh-CN;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5
Cache-Control: max-age=0
Connection: keep-alive
Cookie: _userCode_=20191272346265901; _userIdentity_=20191272346264157; _tt_=821EF180C19DF98BCCF469F73DB1D69A; __utmz=196937584.1575733587.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); DefaultCity-CookieKey=364; DefaultDistrict-CookieKey=0; _ydclearance=333525a9207dab7f7264599a-06f8-4ec6-b4a1-9dcaba5ddba6-1575907320; __utma=196937584.1593013846.1575733587.1575733587.1575900120.2; __utmt=1; __utmt_~1=1; maxShowNewbie=1; yd_cookie=4b488d94-05d9-4ba5893b50b63689a56315fdfa7ff891a9a4; __utmc=196937584; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1575733587,1575900121,1575900921; homePageType=B; userId=0; defaultCity=%25E5%25B9%25BF%25E4%25B8%259C%257C364; strIdCity=China_Beijing; __utmb=196937584.26.10.1575900120; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1575901246
Host: www.mtime.com
Referer: http://www.mtime.com/top/tv/top100/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'''

headers = dict([line.split(": ",1) for line in headers.split("\n")])
print(headers)