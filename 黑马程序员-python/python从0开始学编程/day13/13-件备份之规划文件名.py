# 1 用户输入目标文件 sound.txt.mp3
old_name = input('请输入您要备份的文件名:')
# print(old_name)

# 2 规划备份文件的名字
# 2.1 提取后缀--找到名字大的点--名字和后缀分类--最右侧的点才是后缀的点--字符串查找某个字串rfind
index = old_name.rfind('.')
# print(index)

# 2.2 组织新名字 = 原名字 + [备份] + 后缀
# 原名字就是字符串中的一部分子串--切片[开始:结束:步长]
# print(old_name[:index])
# print(old_name[index:])
new_name = old_name[:index] + '[备份]' + old_name[index:]
# print(new_name)

# 3 备份文件写入数据(数据和原文件一样)
