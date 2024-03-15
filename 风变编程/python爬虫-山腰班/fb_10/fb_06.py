import requests,time,smtplib,schedule
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

def weather():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = 'http://www.weather.com.cn/weather/101281601.shtml'
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    suops = BeautifulSoup(res.text,'html.parser').find('ul',class_='t clearfix')
    wea = suops.find(class_='wea')
    tem = suops.find(class_='tem')
    return '今天的天气:{}\n气温:{}'.format(wea.text,tem.text.strip())

def send_mail():
    mailhost = 'smtp.casc.ac.cn'
    cascmail = smtplib.SMTP()
    cascmail.connect(mailhost,25)
    account = 'czl@casc.ac.cn'
    password = 'idc888888'
    cascmail.login(account, password)
    receiver = '344319484@qq.com'
    message = MIMEText(weather(),'plain','utf-8')
    subject = '每日天气'
    message['Subject'] = Header(subject,'utf-8')
    try:
        cascmail.sendmail(account,receiver,message.as_string())
        return '邮件发送成功'
    except:
        return '邮件发送失败'
    cascmail.quit()

def job():
    print('第一次发送')
    send_mail()
    print('发送成功')

schedule.every(5).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(2)