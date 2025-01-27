message_list = []

with open('10.20.21-22.x.txt', 'r') as f:
    messages = f.readlines()
    for message in messages:
        mes = message.strip() + ' 天津-'
        message_list.append(mes.strip())

print(message_list)

with open('10.20.21-22.x-new.txt', 'w') as s:
    for i in message_list:
        a = i + "\n"
        s.writelines(a)
