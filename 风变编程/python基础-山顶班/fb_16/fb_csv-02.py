import csv

with open('test(1).csv', newline = '', encoding = 'utf-8')  as f:
    #参数encoding = 'utf-8'防止出现乱码
    reader = csv.reader(f)
    for row in reader:
        print(row)