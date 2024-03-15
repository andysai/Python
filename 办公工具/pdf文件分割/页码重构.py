f = open('config.txt', 'w')
for i in range(1, 11):
    num = str(i) + "-" + str(i) + "\n"
    f.write(num)
f.close()
