import threading
import time
import socket
import psutil

def thread1():
    # -*-coding:utf-8-*-
    import pywifi, time
    from pywifi import const

    # 1、python连接WiFi，需要使用pywifi包，安装pywifi：pip install pywifi
    # 注意：如果提示找不到comtypes，则还需要安装pip install comtypes
    # 2、判断wifi连接状态：
    def wifi_connect_status():
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]  # acquire the first Wlan card,maybe not

        if iface.status() in [const.IFACE_CONNECTED, const.IFACE_INACTIVE]:
            print("wifi connected!")
            return 1
        else:
            print("wifi not connected!")
        return 0

    # 3、扫描wifi：
    def scan_wifi():
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]

        iface.scan()
        time.sleep(1)
        basewifi = iface.scan_results()

        for i in basewifi:
            print("wifi scan result:{}".format(i.ssid))
            print("wifi device MAC address:{}".format(i.bssid))
        return basewifi

    # 4、连接指定的wifi：
    def connect_wifi():
        wifi = pywifi.PyWiFi()
        ifaces = wifi.interfaces()[0]
        print(ifaces.name())  # 输出无线网卡名称
        ifaces.disconnect()
        time.sleep(3)

        profile = pywifi.Profile()  # 配置文件
        profile.ssid = "cosmolady-office"  # wifi名称
        profile.auth = const.AUTH_ALG_OPEN  # 需要密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = "dslr2021"  # wifi密码

        ifaces.remove_all_network_profiles()  # 删除其它配置文件
        tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
        ifaces.connect(tmp_profile)
        time.sleep(5)
        isok = True

        if ifaces.status() == const.IFACE_CONNECTED:
            print("connect successfully!")
        else:
            print("connect failed!")
        time.sleep(1)
        return isok

    # 5、测试
    def main():
        print("start")
        wifi_connect_status()
        scan_wifi()
        connect_wifi()
        print("finish!")

    if __name__ == "__main__":
        main()
        dic = psutil.net_if_addrs()
        for adapter in dic:
            snicList = dic[adapter]
            mac = '无 mac 地址'
            ipv4 = '无 ipv4 地址'
            ipv6 = '无 ipv6 地址'
            for snic in snicList:
                if snic.family.name in {'AF_LINK', 'AF_PACKET'}:
                    mac = snic.address
                elif snic.family.name == 'AF_INET':
                    ipv4 = snic.address
                elif snic.family.name == 'AF_INET6':
                    ipv6 = snic.address
            # print('%s, %s, %s, %s' % (adapter, mac, ipv4, ipv6))
            if adapter == "WLAN":
                print(ipv4)



def thread2():
    # -*-coding:utf-8-*-
    import pywifi, time
    from pywifi import const

    # 1、python连接WiFi，需要使用pywifi包，安装pywifi：pip install pywifi
    # 注意：如果提示找不到comtypes，则还需要安装pip install comtypes
    # 2、判断wifi连接状态：
    def wifi_connect_status():
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]  # acquire the first Wlan card,maybe not

        if iface.status() in [const.IFACE_CONNECTED, const.IFACE_INACTIVE]:
            print("wifi connected!")
            return 1
        else:
            print("wifi not connected!")
        return 0

    # 3、扫描wifi：
    def scan_wifi():
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]

        iface.scan()
        time.sleep(1)
        basewifi = iface.scan_results()

        for i in basewifi:
            print("wifi scan result:{}".format(i.ssid))
            print("wifi device MAC address:{}".format(i.bssid))
        return basewifi

    # 4、连接指定的wifi：
    def connect_wifi():
        wifi = pywifi.PyWiFi()
        ifaces = wifi.interfaces()[0]
        print(ifaces.name())  # 输出无线网卡名称
        ifaces.disconnect()
        time.sleep(3)

        profile = pywifi.Profile()  # 配置文件
        profile.ssid = "cosmolady-office"  # wifi名称
        profile.auth = const.AUTH_ALG_OPEN  # 需要密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = "dslr2021"  # wifi密码

        ifaces.remove_all_network_profiles()  # 删除其它配置文件
        tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
        ifaces.connect(tmp_profile)
        time.sleep(5)
        isok = True

        if ifaces.status() == const.IFACE_CONNECTED:
            print("connect successfully!")
        else:
            print("connect failed!")
        time.sleep(1)
        return isok

    # 5、测试
    def main():
        print("start")
        wifi_connect_status()
        scan_wifi()
        connect_wifi()
        print("finish!")

    if __name__ == "__main__":
        main()
        dic = psutil.net_if_addrs()
        for adapter in dic:
            snicList = dic[adapter]
            mac = '无 mac 地址'
            ipv4 = '无 ipv4 地址'
            ipv6 = '无 ipv6 地址'
            for snic in snicList:
                if snic.family.name in {'AF_LINK', 'AF_PACKET'}:
                    mac = snic.address
                elif snic.family.name == 'AF_INET':
                    ipv4 = snic.address
                elif snic.family.name == 'AF_INET6':
                    ipv6 = snic.address
            # print('%s, %s, %s, %s' % (adapter, mac, ipv4, ipv6))
            if adapter == "WLAN":
                print(ipv4)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    start_time = time.time()
    t1.start()
    t2.start()
    # 时间非常小，是运行代码的时间差，而不是2秒
    # 这样运行一共有三个线程，主线程和其它两个子线程（thread1、thread2），而且是并行的，子线程启动后，主线程仍然往下运行，因此时间不是2秒
    # 守护线程（主线程退出，子线程就会kill掉）
    print('end_time:{}'.format(time.time()-start_time))
