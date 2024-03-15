import psutil

# 监控cpu
# 获取CPU(逻辑CPU的平均)占用时间的详细信息
print("CPU(逻辑CPU的平均)占用时间的详细信息:\n" + str(psutil.cpu_times()) + "\n")
# 获取每个CPU占用时间的相信信息
print("每个CPU占用时间的相信信息:\n" + str(psutil.cpu_times(percpu=True)) + "\n")
# CPU逻辑数量
print("CPU逻辑数量:" + str(psutil.cpu_count()) + "\n")
# CPU物理数量
print("CPU物理数量:" + str(psutil.cpu_count(logical=False)) + "\n")
# CPU占比
print("CPU占比:" + str(psutil.cpu_percent()) +"\n")
# 每个CPU占比
print("每个CPU占比:\n" + str(psutil.cpu_percent(percpu=True)) + "\n")

# 监控内存
print("内存信息:" + str(psutil.virtual_memory()) + "\n")
# 监控硬盘
print("硬盘信息:\n" + str(psutil.disk_partitions()) + "\n")
# 磁盘使用情况
print("磁盘使用情况:" + str(psutil.disk_usage('C:\\')) + "\n")

# 监控网络
# 获取网络读写字节/包的个数
print("网络读写字节/包的个数:\n" + str(psutil.net_io_counters()) + "\n")
# 获取网络接口信息
print("网络接口信息:\n" + str(psutil.net_if_addrs()) + "\n")
# 获取网络接口状态
print("网络接口状态:\n" + str(psutil.net_if_stats()) + '\n')
# 获取当前网络连接信息
print("当前网络连接信息:\n" + str(psutil.net_connections()) + '\n')

# 获取进程信息
for pid in psutil.pids():
    print(pid, end=',')
# 查找微信程序相关信息
# for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
#     if proc.info['name'].startswitch('WeChat'):
#         print(proc.info)

#
