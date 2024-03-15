"""
总结
    打开
        文件对象 = open(目标文件, 访问模式)
    操作
        读
            文件对象.read()
            文件对象.readlines()
            文件对象.readline()
        写
            文件对象.write()
        seek()
    关闭
        文件对象.close()

    主访问模式
        w:写,文件不存在则新建该文件
        r:读,文件不存在则报错
        a:追加
    文件和文件夹操作
        重命名:os.rename()
        获取当前目录:os.getcwd()
        获取当前列表:os.listdir()
"""