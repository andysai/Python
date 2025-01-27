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
stdin, stdout, stderr = ssh.exec_command("kubectl get ns | awk {'print $1'}")

# 将表空间数据存放到列表
ns_lists = stdout.read().decode().splitlines()[1:]

# print(len(ns_lists))

# 去掉空的表空间
ns_use_lists = []
for ns_list in ns_lists:
    if ('kube-node-lease' != ns_list and 'default' != ns_list
            and 'kube-public' != ns_list and 'sp-product' != ns_list and 'mpsr-product' != ns_list):
        ns_use_lists.append(ns_list)

ns_product_lists = []
ns_system_lists = []
for message in ns_use_lists:
    # 统计项目表空间
    if 'ingress-nginx' == message or 'kube-system' == message or 'kuboard' == message or 'selenium-grid' == message:
        ns_system_lists.append(message)
    else:
        # 统计系统表空间
        ns_product_lists.append(message)


# 获取 k8s 项目容器的数据
for ns_name in ns_product_lists:
    # 获取容器名称跟状态
    pods_name_stdin, pods_name_stdout, pods_name_stderr = ssh.exec_command(
        "kubectl get pods -n " + ns_name + " -o wide | awk {'print $1'} | grep -v 'NAME'")
    pods_ip_stdin, pods_ip_stdout, pods_ip_stderr = ssh.exec_command(
        "kubectl get pods -n " + ns_name + " -o wide | awk {'print $6'} | grep -v 'IP'")
    pods_node_name_stdin, pods_node_name_stdout, pods_node_name_stderr = ssh.exec_command(
        "kubectl get pods -n " + ns_name + " -o wide | awk {'print $7'} | grep -v 'NODE'")
    pods_status_stdin, pods_status_stdout, pods_status_stderr = ssh.exec_command(
        "kubectl get pods -n " + ns_name + " -o wide | awk {'print $3'} | grep -v 'STATUS'")

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
            docker_list.insert(3, '10.12.13.93')
        elif docker_list[2] == 'node02':
            docker_list.insert(3, '10.12.13.94')
        elif docker_list[2] == 'node03':
            docker_list.insert(3, '10.12.13.95')
        elif docker_list[2] == 'node04':
            docker_list.insert(3, '10.12.13.96')
        elif docker_list[2] == 'node05':
            docker_list.insert(3, '10.12.13.97')
        elif docker_list[2] == 'node06':
            docker_list.insert(3, '10.12.13.98')
        elif docker_list[2] == 'node07':
            docker_list.insert(3, '10.12.13.83')

        # 将数据保存到列表
        messages_list.append(docker_list)

    # print(messages_list)
    for message in messages_list:
        print(message)
















# # 关闭远程连接
# ssh.close()
# list_a = []
#
# for i in status_list:
#     test = i.replace(" ", ",")
#     print(test.split())
#
#
# # 创建实例
# app = xw.App(visible=True, add_book=False)
#
# # 打开工作簿
# workbook = app.books.add()
#
# # 筛选并添加数据
# # 1.1 获取所有表格数据
# sheets_list = workbook.sheets
#
# # 1.2 将筛选的数据存入列表
# # 新增工作表
# qhs_excle = workbook.sheets.add("docker")
#
# # 1.3 列表数据加入新表格
# # 添加标题
# qhs_excle.range("A1:E1").value = ['容器名称', '运行节点', '节点IP', '容器IP', '状态']
#
# # 数据处理
# messages_list = []
# for message in status_list:
#     messages_list.append(message.replace(" ", ",").splitlines())
#
#
# flag = 1
# for i in messages_list:
#     flag += 1
#     # 获取行
#     str_sheet1 = "A" + str(flag) + ":" + "E" + str(flag)
#     qhs_excle.range(str_sheet1).value = i
#

# 保存数据
# workbook.save("get_docker.xlsx")

# 关闭工作表
# workbook.close()

# 关闭工作簿
# app.quit()
