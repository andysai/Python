import functools
EX5_IP_lists = []
zy_IP_lists = []
with open ('EX5_IP.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        EX5_IP_lists.append(i.strip())
    #EX5_IP_lists = f.readlines()
    f.close()

with open ('zy_IP.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        zy_IP_lists.append(i.strip())
    f.close()

#print(len(EX5_IP_lists))
#print(zy_IP_lists)

for i in zy_IP_lists:
    if i not in EX5_IP_lists:
        print(i)