ip_list = []
with open('./中国大陆ip集.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        ip_list.append(i.replace("\n", ""))
    f.close()

print(ip_list)
print(len(ip_list))

i = '1.0.1.0-1.0.4.0'
print(i.split("."))
