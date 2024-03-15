"""
# 获取未读邮件
unread_inbox_messages = imbox.messages(unread=True)
# 获取星标邮件
inbox_flagged_messages = imbox.messages(flagged=True)
# 查看某个发件人的邮件
inbox_message_from = imbox.messages(send_from="某个人的邮件账号")
# 查看某个收件人的邮件
inbox_message_to = imbox.messages(sent_to="某个人的邮件账号")
# 通过日期筛选邮件，需要导入datatime日期模块
# date__lt:表示某一天前 date__gt:表示某天后 date__on:表示某一天
inbox_messages_received_before = imbox.messages(date__lt=datetime.date(2020,6,20))
inbox_messages_received_after = imbox.messages(date__gt=datetime.date(2020,6,20))
inbox_messages_received_on_date = imbox.messages(date__on=datetime.date(2020,6,20))
"""

# 导入模块
from imbox import Imbox
import keyring

# 读取keying密码
pwd = keyring.get_password('yagmail','344319484@qq.com')
# 查看所有邮件
with Imbox('imap.qq.com', '344319484@qq.com', pwd, ssl=True) as imbox:
    all_inbox_messages = imbox.messages()
    for uid, message in all_inbox_messages:
        print(message.subject)
        print(message.body['plain'])
