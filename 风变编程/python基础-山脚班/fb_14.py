import random
import time
def lucyly(luckylist):
    # 提示：将以下部分封装进函数
    a = random.choice(luckylist)
    print('开奖倒计时',3)
    time.sleep(1)
    print('开奖倒计时',2)
    time.sleep(1)
    print('开奖倒计时',1)
    time.sleep(1)
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)
    print('恭喜'+a+'中奖！')

lucyly(['海绵宝宝','派大星','章鱼哥'])