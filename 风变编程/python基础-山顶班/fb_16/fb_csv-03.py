import csv
with open('test(1).csv','test_1', newline='',encoding='utf-8') as f:
    writer  = csv.writer(f)
    #['4', '猫砂', '25', '1022', '886']
    writer.writerow(['4', '猫砂', '25', '1022', '886'])
    #['5', '猫罐头', '18', '2234', '3121']
    writer.writerow(['5', '猫罐头', '18', '2234', '3121'])
print('写入完毕')