import paramiko

# 创建ssh客户端
ssh = paramiko.SSHClient()

# 密码认证
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 服务器相关信息
ip = '10.12.12.203'
port = 22
username = 'root'
password = "Dslr*2022!@#"

# 连接服务器
ssh.connect(hostname=ip, port=port, username=username, password=password)

# 查看所有镜像
stdin, stdout, stderr = ssh.exec_command("docker images | grep 'harbor.cosmo-lady.com'")

# 输出所有的镜像内容
messages = stdout.read().splitlines()

# 将所有查询到的数据存放在 images_lists 列表中
images_lists = []
for message in messages:
    images_lists.append(message.decode().split())

images_list = []
for image_list in images_lists[1:]:
    images_list.append(image_list)

images_id = []
# 获取对应的镜像名称、镜像版本、镜像ID
for image_list in images_list:

    # 获取版本信息为 none 的镜像 ID
    if image_list[1] == '<none>':
        images_id.append(image_list[2])
        version_message = "镜像名称：" + image_list[0] + "\n" + "镜像版本：" + image_list[1] + "\n" + "镜像ID：" + image_list[2] + "\n"
        print(version_message)

# 数据拼接
image_id = ' '.join(images_id)
message = "docker rmi " + image_id

# 执行无效镜像删除操作
# stdin1, stdout1, stderr1 = ssh.exec_command(message)
#
# # 打印日志
# print(stdout1.read().decode('utf-8'))

# 关闭远程 SSH 连接
ssh.close()
