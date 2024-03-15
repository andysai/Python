# 需要使用到SMTPLIB库，来进行邮箱的连接
import smtplib
# 处理邮件内容的库，email.mime
from email.mime.text import MIMEText
# 邮箱编码器
from email import encoders
# 处理邮件附件，需要导入MIMEMultipart，Header，MIMEBase
from email.mime.multipart import MIMEMultipart
# 国际化标题
from email.header import Header
from email.mime.base import MIMEBase
import keyring

# 获取授权码
pwd = keyring.get_password("yagmail", "344319484@qq.com")

#邮件正文内容
contents = '安能摧眉折腰事权贵，使我不得开心颜'
email = MIMEText(contents, 'plain', 'utf-8')

# 定义邮件主题
email['Subject'] = '没有附件的邮件'
# 发件人
email['From'] = '344319484@qq.com'
# 收件人
email['To'] = 'czl@casc.ac.cn'

# 发送邮件
smtp = smtplib.SMTP_SSL('smtp.qq.com', port=465)
smtp.login('344319484@qq.com', pwd)
smtp.sendmail('344319484@qq.com', 'czl@casc.ac.cn', email.as_string())
smtp.quit()
print('发送成功')
