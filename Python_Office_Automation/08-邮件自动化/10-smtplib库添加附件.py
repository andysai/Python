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
pwd = keyring.get_password('yagmail', '344319484@qq.com')

# 构造邮件对象MIMEMultipart对象
email = MIMEMultipart()
email['Subject'] = '带有附件的邮件'  # 定义邮件主题
email['From'] = '344319484@qq.com'  # 发件人
email['To'] = 'czl@casc.ac.cn'  # 收件人

#邮件正文内容
contents = '安能摧眉折腰事权贵，使我不得开心颜'
att = MIMEText(contents, 'plain', 'utf-8')
email.attach(att)
# txt附件
att1 = MIMEBase('application', 'octet-stream')
# set_payload读取数据
att1.set_payload(open('source_material/附件.txt', 'rb').read())
# 设置编码格式，和附件重命名成xxx.txt
att1.add_header('Content-Disposition', 'attachment', filename=Header('附件.txt', 'utf-8').encode())
encoders.encode_base64(att1)
email.attach(att1)

# 发送邮件
smtp = smtplib.SMTP_SSL('smtp.qq.com', port=465)
smtp.login('344319484@qq.com', pwd)
smtp.sendmail('344319484@qq.com', 'czl@casc.ac.cn', email.as_string())
smtp.quit()
print('发送成功')
