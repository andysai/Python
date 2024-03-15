# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
a = 0
number = []
test = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            number.append(str(i) + str(j) + str(k))
            for l in number:
                if l not in test:
                    test.append(l)
                    a += 1
print(test)
print(a)