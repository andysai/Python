# 导入paramiko，（导入前需要先在环境里安装该模块）
import paramiko

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

# 查看k8s表空间，并添加到列表
stdin, stdout, stderr = ssh.exec_command("kubectl get ns | awk {'print $1'} | grep -v 'NAME'")
ns_lists = stdout.read().decode().splitlines()

# 获取容器数据
# bms-test
get_pods_list = []
pods_name_stdin, pods_name_stdout, pods_name_stderr = ssh.exec_command("kubectl get pods -n vim-product -o wide | awk {'print $1'} | grep -v 'NAME'")
pods_ip_stdin, pods_ip_stdout, pods_ip_stderr = ssh.exec_command("kubectl get pods -n vim-product -o wide | awk {'print $6'} | grep -v 'IP'")
pods_node_name_stdin, pods_node_name_stdout, pods_node_name_stderr = ssh.exec_command("kubectl get pods -n vim-product -o wide | awk {'print $7'} | grep -v 'NODE'")
pods_status_stdin, pods_status_stdout, pods_status_stderr = ssh.exec_command("kubectl get pods -n vim-product -o wide | awk {'print $3'} | grep -v 'STATUS'")

# 将数据存放到列表
pods_name_list = pods_name_stdout.read().decode().splitlines()
pods_ip_list = pods_ip_stdout.read().decode().splitlines()
pods_node_name_list = pods_node_name_stdout.read().decode().splitlines()
pods_status_list = pods_status_stdout.read().decode().splitlines()

# 数据合并
docker_lists = zip(pods_name_list, pods_ip_list, pods_node_name_list, pods_status_list)

# 空列表，用来存放所有需要的数据
messages_list = []

for i in docker_lists:
    # 转为列表
    docker_list = list(i)
    # 判断容器部署的物理服务器
    if docker_list[2] == 'node01':
        docker_list.insert(3, '10.12.12.93')
    elif docker_list[2] == 'node02':
        docker_list.insert(3, '10.12.12.94')
    elif docker_list[2] == 'node03':
        docker_list.insert(3, '10.12.12.95')
    elif docker_list[2] == 'node04':
        docker_list.insert(3, '10.12.12.96')
    elif docker_list[2] == 'node05':
        docker_list.insert(3, '10.12.12.97')
    elif docker_list[2] == 'node06':
        docker_list.insert(3, '10.12.12.98')
    elif docker_list[2] == 'node07':
        docker_list.insert(3, '10.12.12.83')

    # 将数据保存到列表
    messages_list.append(docker_list)

print(messages_list)
