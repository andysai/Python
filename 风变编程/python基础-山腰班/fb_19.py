# 一、按照一下要求定义一个游乐园门票类，并尝试计算2个成人+1个小孩子平日票价
# 1.平日票价100元
# 2.周末票价为平日票价120%
# 3.儿童半价

# 1.定义一个门票的类
class Ticket:
    # 2.定义
    def __init__(self,adult_number,kid_number):
        self.adult_number = adult_number
        self.kid_number = kid_number

    # 默认的票价为承认的票价
    def Price(self,adult_number,kid_number=1,price=100):
        weekend = input("请问是否是周末(是/否):")
        if weekend == '是':
            one_adult_price = price * 1.2
            all_adult_price = one_adult_price * adult_number  # 成人票价
            one_kid_price = one_adult_price / 2
            kid_price = one_kid_price * kid_number  # 儿童票价
            ALL_price = all_adult_price + kid_price
            message = '由于是周末,票价上涨20%,成年人票价为:{}元/张,成年人购票数量为:{}张,小孩票价为:{}元/张,小孩购票数量为:{}张,总价为:{}元'. \
                format(one_adult_price, adult_number, one_kid_price, kid_number, ALL_price)
            return message
        elif weekend == '否':
            adult_price = price * adult_number  # 成人票价
            one_kid_price = price / 2
            kid_price = one_kid_price * kid_number  # 儿童票价
            ALL_price = adult_price + kid_price
            message = '由于不是周末,票价不变,成年人票价为:{}元/张,成年人购票数量为:{}张,小孩票价为:{}元/张,小孩购票数量为:{}张,总价为:{}元'. \
                format(price, adult_number, one_kid_price, kid_number, ALL_price)
            return message
        else:
            return '请按照提示内容输入'

manber = Ticket
print(manber.Price(2,1))