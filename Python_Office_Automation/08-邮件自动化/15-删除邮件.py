from imbox import Imbox
import keyring
# 读取keying密码
pwd = keyring.get_password('yagmail','344319484@qq.com')
# 查看所有邮件
with Imbox('imap.qq.com', '344319484@qq.com', pwd, ssl=True) as imbox:
    all_inbox_messages = imbox.messages()
    for uid, message in all_inbox_messages:
        if message.subject == '带有附件的邮件':
            print('匹配成功')
            imbox.delete(uid)
            print("删除成功")
        else:
            print("不存在该邮件")
            break
