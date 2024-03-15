#! python3
# coding=utf-8

import requests
import json

def searchPackage():
    packageNum = input("请输入快递单号：")
    url1 = "http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=" +packageNum
    url1_html = requests.get(url1).text
    comCode = json.loads(url1_html)['auto'][0]['comCode'] #用packageNum找快递公司
    url2 = 'http://www.kuaidi100.com/query?type=' + comCode + '&postid=' + packageNum + '&temp=0.6131059823535396'
    url2_html = requests.get(url2).text #用快递公司查找物流信息
    result = json.loads(url2_html)
    print('时间↓  物流信息↓\n')
    for item in result('data'):
        print(item['time'],item['context'])

searchPackage()