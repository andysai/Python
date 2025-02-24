# 引用模块
import csv

# 调用open()函数打开csv文件，传入参数:文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'
csv_file = open('demo.csv','w',newline='',encoding='utf-8')
# 用csv.writer()函数创建一个writer对象
writer = csv.writer(csv_file)
# 调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “电影”和“豆瓣评分”
writer.writerow(['电影','豆瓣评分'])
# 在csv文件里写入一行文字 “银河护卫队”和“8.0”
writer.writerow(['银河护卫队','8.0'])
# 在csv文件里写入一行文字 “复仇者联盟”和“8.1”
writer.writerow(['复仇者联盟','8.1'])
# 写入完成后，关闭文件就大功告成啦！
csv_file.close()

csv_file = open('demo.csv','r',newline='',encoding='utf-8')
reader = csv.reader(csv_file)
for i in reader:
    print(i)
csv_file.close()