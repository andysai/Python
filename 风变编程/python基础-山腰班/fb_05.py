import random

punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = input('请选择要出的拳(石头,剪刀,布):')

if computer_choice == user_choice :
    print(computer_choice,user_choice)
    print('平局')
elif ((computer_choice == '石头') and (user_choice == '布')) or ((computer_choice == '布') and (user_choice == '剪刀')) \
        or ((computer_choice == '剪刀') and (user_choice == '石头')):
    print('玩家胜利')
elif ((computer_choice == '石头') and (user_choice == '剪刀')) or ((computer_choice == '剪刀') and (user_choice == '布')) \
        or ((computer_choice == '布') and (user_choice == '石头')):
    print('电脑胜利')
print('电脑出的是:%s,玩家出的是:%s' % (computer_choice,user_choice))