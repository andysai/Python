import smtplib
from email.mime.text import MIMEText
from email.header import Header
import fb_02
mailhost = 'smtp.casc.ac.cn'
cascmail = smtplib.SMTP()
cascmail.connect(mailhost,25)
account = 'czl@casc.ac.cn'
password = 'idc888888'
cascmail.login(account,password)
receiver = '344319484@qq.com'
content = fb_02.wea
message = MIMEText(content,'plain','utf-8')
subject = '每日天气'
message['Subject'] = Header(subject,'utf-8')
try:
    cascmail.sendmail(account,receiver,message.as_string())
    print('邮件发送成功')
except:
    print('邮件发送失败')
cascmail.quit()