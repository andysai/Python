"""
1 出拳
    玩家：手动输入
    电脑：1 随机
            1 导入模块
                import random
            2 使用这个模块中的功能
                random.randint()
2 判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜

"""
import random
# 1 出拳
# 玩家
player = int(input("请出拳(0--石头;1--剪刀;2--布):"))
# 电脑
computer = random.randint(0,2)

# 2 判断输赢
# 玩家获胜
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)) :
    print('玩家获胜')
# 平局
elif player ==  computer:
    print('平局，别走，再来一次')
# 电脑获胜
else:
    print('电脑获胜')