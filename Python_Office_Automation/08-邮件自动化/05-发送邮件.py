# 导入模块
import yagmail

# yagmail.SMTP(user="用户名", host="SMTP服务器域名")
yag = yagmail.SMTP(user="344319484@qq.com", host="smtp.qq.com")

# 正文内容
contents = ['大江东去浪淘尽', '千古风流人物']

subject = '三国演义主题曲'

yag.send('czl@casc.ac.cn', subject, contents)
yag.close()
print('发送成功')
