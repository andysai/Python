import random
# 1.程序名称“帮你做选择”
print('帮你做选择')
# 2.先定制一个系统的菜单
while True:
    menu = ('西红柿炒鸡蛋', '牛肉面', '小米粥')
    chooice = random.randint(0, 3)
    if chooice == 0:
        print(menu[chooice])
    elif chooice == 1:
        print(menu[chooice])
    elif chooice == 2:
        print(menu[chooice])
    like = input('请问是否喜欢推荐的菜(是/否):')
    if like == '是':
        break