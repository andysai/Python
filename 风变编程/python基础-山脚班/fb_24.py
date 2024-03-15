# 十、编写一个名为make_album()函数，
# 它创建一个描述音乐专辑的字典，
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实该字典正确地存储了专辑的信息

def make_album(data):
    music_dict = {}
    music_dict.update(data)
    return music_dict
mess = {'梦佳':'糖果','筷子兄弟':'小苹果','逃跑计划':'夜空中最亮的星'}
print(make_album(mess))
mess1 = {'梦佳':'糖果'}
print(make_album(mess1))