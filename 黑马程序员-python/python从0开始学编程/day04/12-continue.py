i = 0
while i < 5:
    i += 1
    if i == 3:
        print('吃出一个大虫子，这个苹果不吃了')
        continue
    print(f'吃了第{i}个苹果')