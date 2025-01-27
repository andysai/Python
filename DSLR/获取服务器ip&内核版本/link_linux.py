#导入paramiko，（导入前需要先在环境里安装该模块）
import paramiko

#定义函数ssh,把操作内容写到函数里
def sshExeCMD():
    # 定义一个变量ssh_clint
    ssh_client = paramiko.SSHClient()
    # 通过这个set_missing_host_key_policy方法用于实现登录是需要确认输入yes，否则保存
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 使用cnnect类来连接服务器
    ssh_client.connect(hostname="10.12.12.192", port=22, username="root", password="dslr#2022")
    # 执行命令
    # stdin, stdout, stderr = ssh_client.exec_command('ansible --version')
    stdin, stdout, stderr = ssh_client.exec_command('ansible --version')
    # 获取命令结果
    print(stdout.read().decode('utf-8'))
    # 关闭连接
    # ssh_client.close()

#通过判断模块名运行上边函数
if __name__ == '__main__':
    sshExeCMD()
