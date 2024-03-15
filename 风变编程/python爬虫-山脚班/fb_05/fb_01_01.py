# 导入模块
import requests
# 判断执行次数
for i in range(5):
    # 网站地址，其中的str(i)是指页码，当页码等于循环的次数将进行页面跳转
    url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum=' + str(i) + '&pagesize=15&lasthotcommentid=song_102065756_3202544866_44059185&domain=qq.com&ct=24&cv=10101010'
    # 调用get方法，下载评论列表
    res_get = requests.get(url)
    # 使用json()方法，将response对象，转为列表/字典
    res_json= res_get.json()
    # 从列表/字典获取需要的数据comment,commentlist
    list_comments = res_json['comment']['commentlist']
    # 遍历评论列表，输出评论信息
    for i in list_comments:
        print(i['rootcommentcontent'])
        print('----------------------')