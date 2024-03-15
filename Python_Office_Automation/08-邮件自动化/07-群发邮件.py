# 导入模块
import yagmail

# yagmail.SMTP(user="用户名", host="SMTP服务器域名")
yag = yagmail.SMTP(user="344319484@qq.com", host="smtp.qq.com")

# 正文内容
contents = ['同学你好！我是咱们学校的XXX，这有一个关于建设图书馆的问卷调查',
            '<a href="https://www.wenjuan.com/new/">图书馆问卷调查</a>',
            '希望你能认真填写，谢谢配合！',
            yagmail.inline('source_material/谢谢.jpg')]

subject = '图书馆问卷调查'

# 发送邮件  yag.send('收件人','邮件标题',邮件内容)
more_mail = ['czl@casc.ac.cn',
             '344319484@qq.com']

yag.send(more_mail, subject, contents)
yag.close()
print('发送成功')
