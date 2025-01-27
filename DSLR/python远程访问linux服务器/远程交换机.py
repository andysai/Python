#导入paramiko，（导入前需要先在环境里安装该模块）
import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.15.255.27", port=22, username="dslr", password="2018_dslr.", look_for_keys=False)
# 执行命令 enable  cisco*.*2018dslr
command = ssh.invoke_shell()
# 配合send()这个函数来对交换机发号施令了
command.send(b"N\n")
command.send(b"en\n")
command.send(b"cisco*.*2018dslr\n")
command.send(b"show run\n")
command.send(b"quit\n")
command.send(b"commit\n")
command.send(b"quit\n")
command.send(b"save\n")
command.send(b"Y\n")
# 前面提到了我们import了time这个模块。有时候系统运行时会有延迟，它的作用是让系统稍侯1秒钟，再执行下面的语句。
time.sleep(1)

# python截屏本次运行后的所有输出记录，将其赋值给output这个变量。
output = command.recv(65535)

# 默认输出为bytes类型的字符串，print出来是单行数据；这里转换为str类型的字符串。
print(str(output, 'utf-8'))

# 关闭连接
ssh.close()
