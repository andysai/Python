'''
一次测评中，老师将 学习小组A 和 学习小组B 的测评成绩(满分 100 分)从低到高记录放进两个列表：
A=[91, 95, 97, 99]，B=[92, 93, 96, 98] 。
现在，老师想将两个小组的成绩合并为一个列表，并按照从低到高的顺序排序，你能帮老师完成吗？
'''
A=[91, 95, 97, 99]
B=[92, 93, 96, 98]
C = A + B
C.sort()
print(C)


print(91+95+97+99+92+93+96+98)