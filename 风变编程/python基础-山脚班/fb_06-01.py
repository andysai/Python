while True:
    a = input('A嫌疑人 你认罪吗？')
    b = input('B嫌疑人 你认罪吗？')
    if  a == '认罪' and b == '认罪' :
        print('太好了，都各判10年')
    elif a == '有罪' and b == '没罪' :
        print('a判1年，b判20年')
    elif a == '没罪' and b == '有罪' :
        print('a判20年，b判1年')
    elif a == '没罪' and b == '没罪' :
        print('各判3年 唉!')
    break