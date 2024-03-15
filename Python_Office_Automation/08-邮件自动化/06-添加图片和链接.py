# 导入模块
import yagmail

# yagmail.SMTP(user="用户名", host="SMTP服务器域名")
yag = yagmail.SMTP(user="344319484@qq.com", host="smtp.qq.com")

# 正文内容
contents = ['说什么王权富贵',
            '怕什么戒律清规',
            yagmail.inline('source_material/草莓.jpg'),
            '<a href="https://www.baidu.com/s?ie=utf-8&wd=%E5%9B%BE%E7%89%87">图片</a>']

subject = '女儿国'

# 发送邮件 yag.send('收件人', '邮件标题', 邮件内容)
yag.send('czl@casc.ac.cn', subject, contents)
yag.close()
print('发送成功')
