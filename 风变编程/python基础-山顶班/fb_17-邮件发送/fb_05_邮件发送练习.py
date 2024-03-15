# smtplib 用于邮件的发信动作
import smtplib
# 内容形式为纯文本、HTML页面
from email.mime.text import MIMEText
# 导入Header模块构建邮件得三个头信息，即From、To、Subject
from email.header import Header
# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = 'czl@casc.ac.cn'
password = 'idc888888'
# 收信方邮箱
to_addr = ['344319484@qq.com']
# 发信服务器
smtp_server = 'mail.casc.ac.cn'
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText('python test mail','plain','utf-8')
# 构建得邮件主题、发件人、收件人信息
msg['From'] = Header(from_addr)
msg['To'] = Header(','.join(to_addr))
msg['Subject'] = Header('Subject')
# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP(smtp_server)
server.starttls()
server.connect(smtp_server,25)
# 登录发信邮箱
server.login(from_addr,password)
# 发送邮件
server.sendmail(from_addr,to_addr,msg.as_string())
# 关闭服务器
server.quit()
