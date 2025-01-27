with open('主机名称.txt', "r") as file:
    messages = file.readlines()

# 可见的名称
with open('主机名称-new.txt', 'w') as host:
    for i in messages:
        # 替换符号
        message = i.replace("-", "_").replace(" ", "-").replace("\n", "") + "\t" + "京东云-Centos7.9-" + i.replace("-", "_").replace(" ", "-")
        host.writelines(message)

