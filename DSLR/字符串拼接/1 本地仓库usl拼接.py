
# 生成a到z的列表
zm_list = [chr(letter).lower() for letter in range(65, 91)]

# 利用for循环进行URL拼接
# for i in zm_list:
#     pinjie = "baseurl=http://192.168.77.128/centos7/cloud/$basearch/openstack-queens/" + i
#     print(pinjie)

# 利用for循环进行URL拼接
# for i in zm_list:
#     pinjie = "baseurl=http://192.168.77.128/centos7/cloud/$basearch/openstack-rocky/" + i
#     print(pinjie)


# 利用for循环进行URL拼接
# for i in zm_list:
#     pinjie = "baseurl=http://192.168.77.128/centos7/cloud/$basearch/openstack-stein/" + i
#     print(pinjie)


# 利用for循环进行URL拼接
for i in zm_list:
    pinjie = "baseurl=http://192.168.77.128/centos7/cloud/$basearch/openstack-train/" + i
    print(pinjie)

