import requests,json

url = 'https://ipassport.ele.me/newlogin/sms/login.do?'
session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
data = {'loginId': '13686635733',
        'phoneCode': '86',
        'countryCode': 'CN',
        'smsCode': '325911',
        'smsToken': 'idc_135A1FCF78F0B40A4BBC2263DA2E7BC8B',
        'keepLogin': 'false',
        'ua': '121#/0ulkPMm0/QlVl2+G89olhKYSkfNTnjVH9Bm4aIH4vu1xlrVj0eklytYxa8dK5jVllKY+zPIDMlSAQQcVFT3ll9YAcWZKujVVmr+4FJ5KM9lOlrJEGiIlMLYAcfdK5jVlmuY+zpIxM9VO3rnEkDIll9YOc8dKkjVlwr7JNtNOwoVG0bvsbc9M98ze0bWkBuMCbibYQhEU960C6Jbnj2SRCD0CZe483VhlRjGprzXF9WbMXF3nnxVp16FlwRT8uzDCbi0CN+SFtFbbZsbnjxSpXb0C60Z8uBmbZs0CeHXF960C60lnW49Exja7icTvOSHGqaxZBNIwdcRQPbinQLSOZsbkX7T83pUVwYQ6MFRD+DQpRgm+QBgngqQniJKOvKkHYksBDeOIUcSE71BatczcARVrzECdYNfKvE6c/N/tn4lwkY5jFZeWAvF/Si3P+QlrzTdfeBfp+QEgEtPd1PPxy4RyX6SWqjGfypencU65B1Ag4W6RJJZvs5wpDHncD/RzZ7S6Y0VS0Gkxun2WDZ6gq4p3ngpCtXV+SPWu7JoTptF9pG28Y4yD76oPbCyJYaht3YzdOqIvsYE+1/v6Pn4ioU0AUgdhI1qoMjKfvoGpt7Sx3joQf2cTbdnxUz6gZSrGKcym2einl6mvdj5q/PzAnXebi2LG+8gTmJkwIKrei+K3tFq5Nm754aeUks6tzaKj8VTI3JnmOGgiUVj64PybWDunlwHzv91qQJn7ALMOi5uiNNcc73lEUdkAe0qDNjm1Q8eZ/FlWA7taKOOhCwgN7tmBF951p/W5D3ykG20ac01yNQSOR0+6K0ERIZ/bUv8cjfAWmR2u34Y4fZsiCxFhqFeDOvAcpLh+Ncg338JigW+NA+aRIjPY8FPhGGXYBc4lrnFUX013w+koosvnpF3LfF2R6lEIlkFmC9npME6kalg04gjlFugSdn8UY4pC0UjtYHKo7bkDbaCvsIozjm4CrybBY6kUEyVvQgKVlrdw1WbhezicZafWNtbCc75gBc8lVhYQ29wcZbLydcKu7F3+4tz7XYmNL+w95XALxmCIRs3jPgYhMDfyDCcIdURYuDUocSpiubV3NnHyqErns+woIR4LyRgYNoVGOfFcedPasQZ43T6uM8m+vIPbhZh9OHkUqMerJdKVKg5TOocTVlzFNsJ6SOJ0sr+tg6xOP1twxI+yOC/5ojPON9OHavfb/bFzZB8wZqVxXjN8ulayzpxV1lJ54UTqxktHHAuKOAaH0Sl4a3fepdkP39ej789sY2CoHCYBrTWgYOV/0UaBLELR2SF2O7hYzfmCvPjsvgcClFQfwwlAZm=', 'umidGetStatusVal': '255', 'screenPixel': '1920x1080', 'navlanguage': 'zh-CN', 'navUserAgent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
        'navPlatform': 'Win32',
        'appEntrance': 'eleme_sms_h5',
        'appName': 'eleme',
        'bizParams': '',
        'csrf_token': 'BBO3DUflyclgFYl4Vjy538',
        'fromSite': '-2',
        'hsiz': '1e46c6f847bf96279371c8132e25ec82',
        'isMobile': 'false',
        'lang': 'zh_CN',
        'mobile': 'false',
        'returnUrl': '',
        'umidToken': 'ace08dab102db9b50d61a3d77355b38f4a9959d7'
        }

session_post = session.post(url,headers=headers,data=data)
# 将cookies保存到文本
session_dict = requests.utils.dict_from_cookiejar(session.cookies)
session_str = json.dumps(session_dict)
session_txt = open('a.txt','w',encoding='utf-8')
session_txt.write(session_str)
session_txt.close()

url_1 = 'https://www.ele.me/restapi/shopping/v1/cities/guess'
res = requests.get(url_1,headers=headers)
res_json = res.json()
print(res_json)