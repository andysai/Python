#money = '20'
#print(int(money)*51.3)
import random
punches = ['石头','剪刀','布']

computer_choice = random.choice(punches)
print(punches.index('剪刀'))
print(punches[punches.index(computer_choice)-1])