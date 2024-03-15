file = open('sources.txt','r',encoding='utf-8')
file_line = file.readlines()
file.close()

final_sources = []

for i in file_line:
    data = i.split()
    sum = 0
    for source in data[1:]:
        sum = sum + int(source)
    result = data[0] + ":" + str(sum) + "\n"
    print(result)
    final_sources.append(result)

winner = open('winner.txt','w',encoding='utf-8')
winner.writelines(final_sources)
winner.close()