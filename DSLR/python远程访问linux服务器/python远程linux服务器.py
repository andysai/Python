# -*- coding:utf-8 -*-

# 导入模块
import paramiko

#调用paramiko模块下的SSHClient()
ssh = paramiko.SSHClient()

#加上这句话不用担心选yes的问题，会自动选上（用ssh连接远程主机时，第一次连接时会提示是否继续进行远程连接，选择yes）
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

server_list = []
password_list = []
with open('服务器ip.txt') as s:
    server_rows = s.readlines()
    for server in server_rows:
        server_list.append(server.strip())

with open('password.txt') as p:
    password_rows = p.readlines()
    for password in password_rows:
        password_list.append(password.strip())

message = dict(zip(server_list, password_list))
print(message)
#连接远程主机，SSH端口号为22
for ip,passwd in message.items():
    ssh.connect(ip, 22, 'root', passwd)
    #执行命令
    stdin, stdout, stderr = ssh.exec_command('ls')
    print(stdout.readlines())
    ssh.close()
