# coding=utf-8
'''
IP反查小工具
http://dns.aizhan.com/index.php?r=index/domains&ip=202.203.208.8&page=1&_=1408264478284
'''
import requests, json, urllib, sys, os
from bs4 import BeautifulSoup


# 获取页面内容
def getPage(ip, page):
    r = requests.get("http://dns.aizhan.com/index.php?r=index/domains&ip=%s&page=%d" % (ip, page))
    return r


# 获取最大的页数
def getMaxPage(ip):
    r = getPage(ip, 1)
    json_data = {}
    json_data = r.json()
    maxcount = json_data[u'conut']
    maxpage = int(int(maxcount) / 20) + 1
    return maxpage


# 获取域名列表
def getDomainsList(ip):
    maxpage = getMaxPage(ip)
    result = []
    for x in range(1, maxpage + 1):
        r = getPage(ip, x)
        result.append(r.json()[u"domains"])
    return result


# 获取最终结果，形式：{url  title}  并写入文件中
def getResultWithTitle(filepath, domain_list):
    f = open(filepath, "a")
    res_dict = {'domain': '', 'title': ''}
    res_list = []
    f.write('<html>')
    for x in domain_list:
        for i in range(0, len(x)):
            title = urllib.urlopen("http://dns.aizhan.com/index.php?r=index/title&id=%d&url=%s" % (i, x[i])).read()
            soup = BeautifulSoup(title)
            res_dict['domain'] = x[i]
            res_dict['title'] = soup.contents[0].encode('utf-8')
            f.write('<a href=' + str(res_dict['domain']) + '>' + str(res_dict['domain']) + '</a>\t\t' + str(
                res_dict['title']) + '<br/>')
            res_list.append(res_dict)
    f.write('</html>')
    f.close()
    return res_list


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:reverseIP targetIP Outfile")
    else:
        ip = str(sys.argv[1])
        outfile = str(sys.argv[2])
        if not str(os.path.basename(outfile)).split('.')[-1] == 'html':
            print("The outfile must end with '.html' ")
        else:
            print("The target IP is :%s" % ip)
            print("Starting, please wait...")
            domainList = getDomainsList(ip)
            getResultWithTitle(outfile, domainList)
getPage('113.105.131.176', 'a.html')
