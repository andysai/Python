import paramiko

def remotConnect():
    # 服务器相关信息,下面输入你个人的用户名、密码、ip等信息
    ip = '10.0.63.14'
    port = 22
    user = "root"
    password = 'Admin@casc.ac.cn'

    # 创建SSHClient 实例对象
    ssh = paramiko.SSHClient()
    # 调用方法，表示没有存储远程机器的公钥，允许访问
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接远程机器，地址，端口，用户名密码
    ssh.connect(ip, port, user, password, timeout=10)
    # 输入linux命令
    filename = '/data1/home/lhlin/jiazi/NMP/20210323-skeletal_muscle.h5ad'
    ls = "cat " + filename
    print(ls)
    stdin, stdout, stderr = ssh.exec_command(ls)
    # 输出命令执行结果
    result = stdout.read()
    print(result)
    # 关闭连接
    ssh.close()

remotConnect()
