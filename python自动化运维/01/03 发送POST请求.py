# 导入 Requests 库
import re

import requests

# 此处使用的接口地址为 zrlog 系统后台登录首页的地址
url_login = "http://zrlog-test.cosmo-lady.com/api/admin/login"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
           'Cookie': '_ati=374880417973'
}

# 请求的数据为 JSON 格式的字符串，并将请求的数据保存在 data 字典中
data = {
    "userName": "admin",
    "password": "Dslr#2024",
    "https": False,
    "key": 1615903975463
}

# 通过 Requests 库发送 POST 请求，其中 verify=False 代表绕过 HTTPS 证书验证
r_res = requests.post(url=url_login, headers=headers, json=data, verify=False)

# 以文本的方式返回响应内容
print(r_res.text)

# 以 JSON 格式返回响应内容
print(r_res.json())
