import requests
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '知乎文章'
sheet['A1'] = '标题'
sheet['B1'] = '链接'
sheet['C1'] = '摘要'

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
offset=0
#设置offset的起始值为0
while True:
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':str(offset),
        'limit':'20',
        'sort_by':'voteups',
        }
    #封装参数
    res=requests.get(url,headers=headers,params=params)
    #发送请求，并把响应内容赋值到变量res里面
    articles=res.json()
    print(articles)
    data=articles['data']
    #定位数据
    for i in data:
        list1=[i['title'],i['url'],i['excerpt']]
        #把目标数据封装成一个列表
        sheet.append(list1)

    offset=offset+20
    #在while循环内部，offset的值每次增加20
    if offset > 40:
        break
wb.save('知乎文章1.xlsx')
#写入完成后，关闭文件就大功告成
print('okay')