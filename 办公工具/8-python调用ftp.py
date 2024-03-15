# 加载ftp模块
from ftplib import FTP
# 设置变量
ftp = FTP()
# 打开调试级别2，显示详细信息
# ftp.set_debuglevel(2)
# 连接的ftp sever和端口
ftp.connect("113.105.137.161", 25804)
ftp.encoding = 'utf-8'
# 连接的用户名，密码
ftp.login("sshftp", "ssh123456")
# 进入远程目录
ftp.cwd("基础数据/微站数据/")
ftp.dir()
# 设置的缓冲区大小
bufsize = 1024
# 需要下载的文件
filename = "万科虹溪诺雅.xlsx"
# 以写模式在本地打开文件
file_handle = open(r'E:\ftp-test\万科虹溪诺雅.xlsx', "wb").write
# 接收服务器上文件并写入本地文件
ftp.retrbinary("RETR filename.txt", file_handle, bufsize)
# 关闭调试模式
ftp.set_debuglevel(0)
# 退出ftp
ftp.quit()
