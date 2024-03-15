#定义两个函数：第一个函数功能为根据工作月数返回奖金额，第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。
#最后传入参数('大聪'，14)调用第二个函数，打印结果'大聪来了14个月，获得奖金2520元'
def month(months):
    if months < 6 :
        return 500
    elif 6 < months < 12 :
        return 120*months
    elif months > 12 :
        return 180*months

def names(name,months):
    message = name + '来了' + str(months) + '个月，获得奖金' + str(month(months)) + '元'
    return message

