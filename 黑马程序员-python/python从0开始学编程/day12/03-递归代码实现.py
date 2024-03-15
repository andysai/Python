# 需求：3以内数字累加和  3 + 2 + 1 = 6
# 6 = 3 + 2以内数字累加和
# 2以内数字累加和 = 2 + 1以内数字累加和
# 1以内数字累加和 = 1 # 出口

# 递归特点：函数内部自己调用自己；必须有出口
def sum_numbers(num):
    if num == 1:
        return 1

    return num + sum_numbers(num - 1)
# 3 + (3-1) = 5
# 2 + (2-1) = 3
# 1 + (1-1) = 1
result_numbers = sum_numbers(3)
print(result_numbers)