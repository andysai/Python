# 导入paramiko，（导入前需要先在环境里安装该模块）
import paramiko
import xlwings as xw

# 创建ssh客户端
ssh = paramiko.SSHClient()

# 密码认证
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 服务器相关信息
ip = '10.12.13.90'
port = 22
username = 'root'
password = "Dslr*2022!@#"

# 连接服务器
ssh.connect(hostname=ip, port=port, username=username, password=password)

# 查看k8s表空间
stdin, stdout, stderr = ssh.exec_command("ls -l")

# 关闭远程连接
ssh.close()
