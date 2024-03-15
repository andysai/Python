# 导入 Requests 库
import requests

# 此处使用的接口地址为 zrlog 系统后台登录首页的地址
url = "https://zrlog-test.cosmo-lady.com/zrlog/"

# 通过 Requests 库发送 GET 请求
r = requests.get(url=url)

# 以文本的方式返回响应内容
print(r.text)

# 返回 HTTP 协议状态码
print(r.status_code)