import paramiko
import time
import datetime
import xlwings as xw

# 服务器相关信息
ip = '10.10.30.228'
port = 22
user = 'root'
passwd = 'Dslr*2022!@#'

# 建立连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, user, passwd, timeout=10)

a = 1
mes_list = []
c_list = []

while a <= 700:
    # 获取当前时间
    nowTime = datetime.datetime.now().strftime("%H:%M:%S")
    # 获取linux负载信息
    stdin_loadavg_1, stdout_loadavg_1, stderr_loadavg_1 = ssh.exec_command("cat /proc/loadavg |awk {'print $1'}")
    stdin_loadavg_5, stdout_loadavg_5, stderr_loadavg_5 = ssh.exec_command("cat /proc/loadavg |awk {'print $2'}")
    stdin_loadavg_15, stdout_loadavg_15, stderr_loadavg_15 = ssh.exec_command("cat /proc/loadavg |awk {'print $3'}")
    stdin_jinc, stdout_jinc, stderr_jinc = ssh.exec_command("cat /proc/loadavg |awk {'print $4'}")
    # 计算负载
    stdin_cpu, stdout_cpu, stderr_cpu = ssh.exec_command("cat /proc/cpuinfo |grep process|wc -l")
    # 获取内存信息
    stdin_free_mem, stdout_free_mem, stderr_free_mem = ssh.exec_command("free -g|head -n 2|tail -n 1 |awk {'print $4'}")
    stdin_free_swap, stdout_free_swap, stderr_free_swap = ssh.exec_command("free -g|tail -n 1 |awk {'print $4'}")
    # 输出命令执行结果
    result_1 = stdout_loadavg_1.read().decode('utf-8').replace("\n", "").strip()
    result_5 = stdout_loadavg_5.read().decode('utf-8').replace("\n", "").strip()
    result_15 = stdout_loadavg_15.read().decode('utf-8').replace("\n", "").strip()
    result_cpu = stdout_cpu.read().decode('utf-8').replace("\n", '').strip()
    result_cpu_1 = round(float(result_1) / float(result_cpu), 2)
    if result_cpu_1 <= 3:
        cpu_xingneng = "系统性能问题良好"
    elif result_cpu_1 >= 3 and result_cpu_1 <= 4:
        cpu_xingneng = "系统性能问题可以接受"
    elif result_cpu_1 > 4:
        cpu_xingneng = "系统性能问题严重"
    result_free_mem = stdout_free_mem.read().decode('utf-8').strip()
    result_free_swap = stdout_free_swap.read().decode('utf-8').strip()

    # 将数据添加到列表
    mes_list.append(nowTime)
    mes_list.append(result_1)
    mes_list.append(result_5)
    mes_list.append(result_15)
    mes_list.append(cpu_xingneng)
    mes_list.append(result_free_mem)
    mes_list.append(result_free_swap)
    c_list.append(mes_list)
    # 将列表的数据情况，以免重复添加
    mes_list = []

    a += 1
    # 每循环一次就暂停5秒
    time.sleep(5)

# 关闭连接
ssh.close()

# 创建实例
app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open(r"./test.xlsx")

# 新增工作表
system_excle = workbook.sheets.add("系统负载数据统计")

# 添加标题
system_excle.range("A1:G1").value = ['时间', '1分钟负载', '5分钟负载', '15分钟负载', '负载情况', '可用内存(G)', '可用SWAP(G)']

for i in range(2, len(c_list)+2):
    # 添加行
    str_address_str = "A" + str(i)
    str_address_end = "G" + str(i)
    # 插入数据
    system_excle.range(str_address_str + ":" + str_address_end).value = c_list[i-2]

# 保存数据
workbook.save(r"./系统负载数据统计-2022-08-15.xlsx")

# 关闭工作表
workbook.close()

# 关闭工作簿
app.quit()


