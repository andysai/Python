# 导入所需的库和模块
from gevent import monkey
monkey.patch_all()
# 让程序变成异步模式
import gevent,requests, bs4, csv
from gevent.queue import Queue

# 获取前3个常见食物类别的前3页食物记录的网址和第11个常见食物类别的前3页食物记录的网址
food_lists = []
for i in range(1,4):
    for j in range(1, 4):
        url = 'http://www.boohee.com/food/group/' + str(i) + '?page=' + str(j)
        url1 = 'http://www.boohee.com/food/view_menu' + '?page=' + str(j)
        food_lists.append(url)
        food_lists.append(url1)

# 创建队列对象，并赋值给work
work = Queue()
# 把构造好的网址用put_nowait添加进队列里
for food_list in food_lists:
    work.put_nowait(food_list)

# 定义crawler函数
def crawler():
    # 添加请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    # 当队列不是空的时候，就执行下面的程序
    while not work.empty():
        # 用get_nowait()方法从队列里把刚刚放入的网址提取出来
        url = work.get_nowait()
        # 用requests.get获取网页源代码
        res = requests.get(url,headers=headers)
        # 用BeautifulSoup解析网页源代码
        suops = bs4.BeautifulSoup(res.text,'html.parser').find_all('li',class_='item clearfix')
        # message_list = []
        # 遍历suops
        for suop in suops:
            # 获取食物名称
            food_name = suop.find('h4').text
            # 获取食物链接
            food_url = 'http://www.boohee.com' + suop.find('test_1')['href']
            # 获取食物热量
            food_calorie = suop.find('p').text[3:]
            # 将上面获取到的数据进行拼接
            message = '\n食物名称:{}\n食物链接:{}\n{}'.format(food_name.strip(),food_url,food_calorie)
            writer.writerow([food_name, food_url, food_calorie])
            #message_list.append(message)
            # 打印结果
            print(message)
        #return message_list

#调用open()函数打开csv文件，传入参数：文件名“boohee.csv”、写入模式“w”、newline=''。
csv_file = open('foods.csv','w',newline='')
# 用csv.writer()函数创建一个writer对象。
writer = csv.writer(csv_file)
#借助writerow()函数往csv文件里写入文字：食物、热量、链接
writer.writerow(['食物', '链接', '热量'])

# 创建空的任务列表
tasks_list = []

# 相当于创建了8个爬虫
for x in range(8):
    # 用gevent.spawn()函数创建执行crawler()函数的任务
    task = gevent.spawn(crawler)
    # 往任务列表添加任务
    tasks_list.append(task)

# 用gevent.joinall方法，启动协程，执行任务列表里的所有任务，让爬虫开始爬取网站
gevent.joinall(tasks_list)
