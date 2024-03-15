import socket

# 创建UDP的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ...这里是使用套接字的功能

# 不用的时候，关闭套接字
s.close()
