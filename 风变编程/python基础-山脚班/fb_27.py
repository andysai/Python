# 实例003：完全平方数
# 题目 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
n=0
while (n+1)**2-n*n<=168:
    n+=1

print(n+1)
