import subprocess
IP_res = []
IP_lists = []
with open('IP.txt', 'r', encoding='utf-8') as f:
    line = f.readlines()
    for i in line:
        IP_lists.append(i.strip())
for ip in IP_lists:
    # windows上cmd的ping操作格式
    res = subprocess.run(['ping', '-n', '1', '-w', '1', ip])

    if res.returncode == 0:
        IP_res.append(ip)
    else:
        print('no')

for i in IP_res:
    print(i)
