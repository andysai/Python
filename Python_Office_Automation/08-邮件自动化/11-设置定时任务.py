import yagmail
import schedule
import time
import datetime

# yagmail.SMTP(user='用户名',host='SMTP服务器域名')
yag = yagmail.SMTP(user='344319484@qq.com', host='smtp.qq.com')

def massage():
    print("开始执行massage函数")
    # 正文内容
    contents = ['大江东去浪淘尽',
                '千古风流人物']
    subject = '三国演义主题曲'
    # 发送邮件  yag.send('收件人','邮件标题',邮件内容)
    yag.send('czl@casc.ac.cn', subject, contents)
    print("success")
# 设置时间
schedule.every().minute.at(":55").do(massage)
while True:
    schedule.run_pending()
    time.sleep(1)
    if datetime.datetime.now().strftime('%H:%M') == '10:13':
        break
yag.close()
print('发送成功')
