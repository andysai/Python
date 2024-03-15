# 导入模块
import requests

# 定义link为网站地址
link = "http://www.santostang.com/"

# 定义请求头的浏览器代理，伪装成浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/88.0.4324.182 '
                         'Safari/537.36 '
                         'Edg/88.0.705.74'}

# 请求网页
r = requests.get(link, headers=headers)

# 获取网页信息
print(r.text)
