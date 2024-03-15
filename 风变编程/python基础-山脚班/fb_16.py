# 1.打印出共进晚餐的嘉宾的名单
hdt = ['sai','andy','king','alice','amy','green']
print('\n-------第一小题--------')
for i in hdt:
    print('你好，{}；请赏脸参加晚上的晚餐，谢谢！'.format(i))

#（2）修改嘉宾名单，你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾
# 2.1 以完成练习（1），为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约
# 2.2 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名
# 2.3再次打印一系列消息，向名单中的每位嘉宾发出邀请
print('\n-------第二小题--------')
print('很遗憾，{}因为有其他紧急的事情需要处理，无法赴约！'.format(hdt[2]))
del hdt[2]
hdt.insert(2,'dawei')
for d in hdt:
    print('你好，{}；请赏脸参加晚上的晚餐，谢谢！'.format(d))

#（3）添加嘉宾，在完成（2）的基础上
# 3.1使用insert()将以为新加冰添加到名单开头
# 3.2使用insert()将另一位新嘉宾添加到名单中间
# 3.3使用append()将最后一位新嘉宾添加到名单末尾
# 3.4打印嘉宾名单
print('\n-------第三小题--------')
hdt.insert(0,'qq')
long = int(len(hdt)/2) #取中间位置
hdt.insert(long,'ss')
hdt.append('ww')
for new1 in hdt:
    print('你好，{}；请赏脸参加晚上的晚餐，谢谢！'.format(new1))

#（4）缩减名单
#4.1 在完成练习（3）的基础上，使用pop不断地删除名单中的嘉宾，直到只有两位为止，并且打印出删除的成员
#4.2 使用del()将最后两位嘉宾从名单中删除，让名单变成空的
while True:
    del1 = hdt.pop()
    print('{}已经被移除'.format(del1))
    if len(hdt) == 2:
        break
print('剩余的宾客有：', hdt)
while True:
    if len(hdt) != 0 :
        del hdt[0]
    else :
        break
print(hdt)