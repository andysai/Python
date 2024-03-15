import requests,json

session =requests.session()
url_1 = 'https://ipassport.ele.me/newlogin/sms/send.do?appName=eleme&fromSite=-2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
data_1 = {
    'phoneCode': '86',
    'loginId': '13686635733',
    'countryCode': 'CN',
    'ua': '121#QWQlk+qbb/MlVl2YG8SPlhKYSkfNAA3VHL0h5ajyYDu1xlrVj0eklytYxa8dK5jVllKY+zPIDMlSAQQcVFT3ll9YAcWZKujVVmr+4FJ5KM9lOlrJEGiIlMLYAcfdK5jVlmuY+zpIxM9VO3rnEkDIll9YOc8dKkjVlwr75zXOIMoVG0bvsbc9M98ze0bWkB5qCbibYQhEU960C6Jbnj2SRCD0CZe483VhlRjGprzXF9WbMXF3nnxVp16FlwRT8uzDCbi0CN+SFtFbbZsbnjxSpXb0C60Z8uBmbZs0CeHXF960C60lnW49ExjaveRTvF/XEQRgJVNIwdcRQPbinQLSOZsbkX7T83pIVwH3OMFRD+ekYqDR7lsvFA5UEhcKly7n7vNYepbwzP+popUxi+Z6QZEVQsZhwJYaHZTYBHFRPot3iFY5zbH8DOiui1GsPlg3g7yp0+nqhjZwlHg6Zbh5DyZEoZa8P43QBI//0sOmDHCA//SDnR1W9yg3ESdOGD3v00IZYoktrCb58EWdSNyrhcJdHbTKglISpJXSdMW2rmOKViVeOzt5U9fzYUul+hix4dldD3aPffYKZpCLqyi8G53E+MgegFiJX1T8uDrPJqra2tok1B3usQ5+clSoWgvy8ZKqENf8Ez4z2WD//Vu5LHRMCZfV6a/yEjfkZnaVtOgbNv7fU8rCmgLNW6/EIMyDfsJomSqFpyR8AYXJHFkYAipdBSVPc5kJNy61BGm3dgtT/l6dGryeKqAPNb2S21a86y9DCjxnKJKO59ajJ/3trUJaN98YZaxuIaPRN6C4p0B7aVuByta8gG/AnzczY57GCdzs1JMq4xgQoC9vInboIjAztZhnf3pjvHQJQ9rWAlxfe5rf5XfEUy8l2xgssYw1lMmLBssglKGe8/gk24IuXM/MV4HtWoBpV+Zq4ECIrgynvTyxkf8IFVcVaxZWSGj7JX181KltVTe3ZLFBhNNV4jSlGHb1n5PbGL5d8kpD6cqWKxmHzOWMbwUwUya4OoQkyPe3Po4WfVuQdrNAXCGTm44wqcCFUOgxUt406fVPiuje/BkKT346Lm+taDBNwh07/FjHdwRldOY10IT1mThx6VIm7g6jext2gyz75/z+ZYuV3/5AWb6oObg8LnLEFZbgKP4umTj5wrdCqS2Vr9wDLBLeH7/Llcaos1l8gxgWZDzeiyP9igLadC23e51U5xu8i5LjCFHnWW2fyDFcZI4YD1DOXk7XQrRoBZeX4fqci87wuP6iFgY9nWutBJtaDNYX7IFAIOW80PZ3T+//TGeBsuAgGKvdw/o=',
    'umidGetStatusVal': '255',
    'screenPixel': '1920x1080',
    'navlanguage': 'zh-CN',
    'navUserAgent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    'navPlatform': 'Win32',
    'appEntrance': 'eleme_sms_h5',
    'appName': 'eleme',
    'bizParams': '',
    'csrf_token': 'oHQQ05Uof2Ct9svyBeTcI4',
    'fromSite': '-2',
    'hsiz': '1f5c0a9a506da2a68e1f8be1c87835ea',
    'isMobile': 'false',
    'lang': 'zh_CN',
    'mobile': 'false',
    'returnUrl': '',
    'umidToken': '2310db0638543b24574dcad6f76e64182ba9500f'
}

res = session.post(url_1, headers=headers, data=data_1).json()
for i in res['content']['data']:
    print(i)
print(res)


