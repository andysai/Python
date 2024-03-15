import requests,openpyxl,random,json
URL = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}
params = {
    'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': '10',
    'limit': '20',
    'sort_by': 'created'
    }

res = requests.get(URL,params=params,headers=headers)
print(res.status_code)
