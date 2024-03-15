import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
work = input('请输入需要翻译的单词:')
data = {
    'i': work,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15754627910321',
    'sign': 'e27312568eabdeddd88c6e4882c73b0b',
    'ts': '1575462791032',
    'bv': 'ec579abcd509567b8d56407a80835950',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
session = requests.post(url,headers=headers,data=data)
res_session = session.json()['translateResult']
for i in res_session:
    src = i[0]['src']
    tgt = i[0]['tgt']
    print('{} 的翻译为 {}'.format(src,tgt))