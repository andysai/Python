# 第一行：必不可少的调用模块。
import time

input("欢迎使用“时间管理器”！请按回车继续。")

while True:
    task_name = input('请输入任务名：')
    task_time = int(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始专注：'%(task_name,task_time))
    # 下面应该要有两行代码，自动记录可以计算以及可以打印的开始时间。
    start = time.time()
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # 这里可以加一个倒计时，实时显示还剩多少时间，可参考左侧提供的资料。代码量大概有5行。
    for t in range(task_time,0,-1):
        info = '请专注任务,还要保持专注 ' + str(t) + '秒哦!'
        print(info,end="")
        print("\b"*(len(info)*2),end="",flush=True)
        time.sleep(1)
    print('你已经专注了 %d 分钟，很棒~再加把劲，完成任务！'%task_time)

    task_status = input('请在任务完成后按输入y:')
    actual_time = input('该任务实际用时为几分钟？')
    if task_status == 'y':
        # 下面应该要有两行代码，自动记录可以计算以及可以打印的结束时间。
        end = time.time()  # 一定用户按了 y，就记下结束时间。
        end_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))  # 日期格式化
        actual_time = int((end -start)/60)  # 始末时间相减，从秒换算到分，除以60。
        start_end = start_time + '——' + end_time + '\n'
        # 有了自动记录的始末时间后，记录的代码也需要随之改变。
        with open('timelog2.txt','test_1', encoding = 'utf-8') as f:
            f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
            f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟\n')
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

print('愿被你善待的时光，予你美好的回赠。')