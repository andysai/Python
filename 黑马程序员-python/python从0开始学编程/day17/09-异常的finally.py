# finally表示的是无论是否异常都要执行的代码，例如关闭文件
# 需求:尝试以r打开一个文件，如果有异常以w打开这个文件，最终关闭文件
try:
    f = open('09_test.txt', 'r')
except Exception as result:
    f = open('09_test.txt', 'w')
finally:
    f.close()