import paramiko

#读取服务器日志，并打印

def get_server_log():
    hostname = "10.0.51.162"
    port = 22
    username = "root"
    password = "Admin@casc.ac.cn"

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname, port, username, password, compress=True)

    remote_command = "tail -n 100 /var/log/messages"

    stdin, stdout, stderr = client.exec_command(remote_command)

    last_line = stdout.read()

    a = last_line.decode('utf-8')

    print(a)

get_server_log()
