# 创建用来存储薪资的空列表
free_list = []

# 循环输入4位员工的薪资
for i in range(1, 5):
    free = input("请输入第" + str(i) + "位员工的薪资:")
    free_list.append(free)
    i += 1

# 统计员工数量
num = len(free_list)

# 计算平均薪资
sum = 0
for j in free_list:
    sum += int(j)
avg = sum / num

print(format(f"{num}人的薪资分别为{free_list},平均薪资为{avg}"))

