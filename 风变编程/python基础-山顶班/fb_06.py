# 下面已经为你准备好了打开的代码和一些变量名的准备。
# 请你完成数据处理以及新建文档（同一个目录）的代码。
# 一个提示：可以用 print 作为检验代码，步步为营。

file1 = open('winner.txt','r',encoding='utf-8')
file_lines = file1.readlines()
file1.close()

dict_scores = {}
list_scores = []
final_scores = []

for i in file_lines:
    print(i)
    name = i[-4:-1]
    source = int(i[-4:-1])
    dict_scores[source] = name
    list_scores.append(source)

list_scores.sort(reverse=True)

for i in list_scores:
    result = str(i) + "\n"
    final_scores.append(result)
print(final_scores)

winner_new = open('winner_new.txt','w',encoding='utf-8')
winner_new.writelines(final_scores)
winner_new.close()