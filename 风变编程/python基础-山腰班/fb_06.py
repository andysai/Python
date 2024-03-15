import random

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = input('请出拳：（石头、剪刀、布:）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()


# 亮拳
print('————战斗过程————')
print('电脑出的是:%s' % computer_choice)
print('玩家出的是:%s' % user_choice)
print('————————————————')

# 胜负
print('—————结果—————')
if user_choice == computer_choice:  # 使用if进行条件判断
    print('平局！')
# 请你将下一行代码用 index()函数 实现（不再有 and 和 or），从而简化代码。
elif user_choice == punches[punches.index(computer_choice)-1]:
    print('你赢了！')
else:
    print('你输了！')
print('————————————————')
