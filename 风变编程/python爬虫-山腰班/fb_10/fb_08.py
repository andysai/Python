import time,requests,schedule,smtplib
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup

def get_foods():
    headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    url = 'http://www.xiachufang.com/explore/'
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    suops = BeautifulSoup(res.text,'html.parser').find_all('div',class_='info pure-u')
    for suop in suops:
        name = suop.find('p').text.strip()
        ing_ellipsis = suop.find('p', class_='ing ellipsis').text.strip()
        link = 'http://www.xiachufang.com' + suop.find('test_1')['href']
        return '菜谱名称:{}\n材料:{}\n链接:{}\n'.format(name,ing_ellipsis,link)

def send_mail():
    mail_host = 'smtp.casc.ac.cn'
    casc_mail = smtplib.SMTP()
    casc_mail.connect(mail_host,25)
    account = ''
    password = ''
    casc_mail.login(account,password)
    receiver = ''
    message = MIMEText(get_foods(),'plain','utf-8')
    subject = '本周最受欢迎食谱'
    message['Subject'] = Header(subject,'utf=8')
    try:
        casc_mail.sendmail(account,receiver,message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    casc_mail.quit()

def job():
    print("开始第一次任务")
    send_mail()
    print("任务完成")

schedule.every().day.at("20:28").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)