lists_24C = []
lists_40C = []
lists_64C = []
lists_16C = []
trusteeship = []
# 统计DELL R720服务器
# 24C
f = open('DELL R720 24C.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    lists_24C.append(list)
f.close()

normal = lists_24C.count('正常') + lists_24C.count('开机')
free = lists_24C.count('空闲') + lists_24C.count('关机')
sum_server = normal + free
print(f'目前DELL R720 24C服务器有{sum_server}台,使用了{normal}台,剩余{free}台')

# 40C
f = open('DELL R720 40C.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    lists_40C.append(list)
f.close()

normal = lists_40C.count('正常')
free = lists_40C.count('空闲') + lists_40C.count('关机')
sum_server = normal + free
print(f'目前DELL R720 40C服务器有{sum_server}台,使用了{normal}台,剩余{free}台')

# DELL R720xd
print(f'目前DELL R720xd服务器有1台,使用了1台,剩余0台')

# DELL R730
print(f'目前DELL R730服务器有3台,使用了2台,剩余1台')

# DELL R730xd
print(f'目前DELL R730xd服务器有1台,使用了1台,剩余0台')

# 统计DELL R910 服务器
f = open('DELL R910 64C.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    lists_64C.append(list)
f.close()

normal = lists_64C.count('正常')
bad = 2
free = lists_64C.count('空闲') + lists_64C.count('关机') - bad
sum_server = normal + free + bad
print(f'目前DELL R910服务器有{sum_server}台,使用了{normal}台,坏了2台,剩余{free}台')

# 统计IBM X3950M2 服务器
f = open('IBM X3950M2.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    lists_16C.append(list)
f.close()

normal = 22 + 14
bad = 57
check = 42
free = 9
sum_server = normal + free + bad + check
print(f'目前IBM X3950M2服务器有{sum_server}台,使用了{normal}台,坏了{bad}台,待测试{check}台,剩余备机{free}台')

# 存储设备-NetStor
print(f'目前NetStor iSum850存储有1台,使用了1台,剩余0台')

# 托管设备
f = open('trusteeship.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    trusteeship.append(list)
f.close()

normal = trusteeship.count('正常') + trusteeship.count('关机') + trusteeship.count('空闲')
sum_server = normal + 200
print(f'目前托管的设备大概有{sum_server}台,客户包括5楼模块4(电子所、遥感黄井优、中科云遥)，2楼模块2(北京地税、北京空间先导、升云、英蓝科技、固云科技、星际无限、自动化所、广州亿扬信息科技有限公司、国云、东莞中科智城软件有限公司、软件所),2楼模块一(英蓝科技)')