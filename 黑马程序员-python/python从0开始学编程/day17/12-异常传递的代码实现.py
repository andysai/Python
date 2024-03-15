# 需求1 : 尝试只读打开12_test.txt 文件存在读取内容，不存在提示用户
# 需求2 : 读取内容:循环读取，当无内容的时候退出循环，如果用户意外终止，提示用户已经被意外终止
import time
try:
    f = open('12_test.txt')
    try:
        while True:
            connect = f.readline()
            if len(connect) == 0:
                break
            time.sleep(2)
            print(connect)
    except:
        # 在命令提示符中如果按下ctrl+c结束终止的键
        print('程序被意外终止')
except:
    print('该文件不存在')