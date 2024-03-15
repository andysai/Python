deposit = [100, 300, 900, 2000, 5000, 0, 2000]


for i in range(1, len(deposit)):
    try:
        times = deposit[i] / deposit[i-1]
        print('你的存款涨了%f倍' % times)
    except ZeroDivisionError:
        print('0不能被除')
