# 使用from 模块名 import 功能 的时候，如果功能名字重复，导入的时候后定义或者后导入的这个同名功能
# 场景 time.sleep()
def sleep():
    print('我是自定义的sleep')

from time import sleep

# 定义函数 sleep
# def sleep():
#     print('我是自定义的sleep')

sleep(2)




