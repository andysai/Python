
# 标准差计算
num = ['18.42',	'30.76', '33.59', '24.11', '28.15', '18.42', '17.91', '12.66']

# 计算中位数
i = 0
mes = 0
while i <= len(num):
    for j in num:
        mes = j + str(mes)
        mes += mes
        i += 1
print(mes)

