ip = '10.12.12.192'
contentList = []

import os
os.system('cls')

def fileReader():
    contentList = []
    with open('a.txt', 'r') as f:
        line = f.readline().rstrip('\n')

    while line != "":
        line = f.readline().rstrip(' \n')
        contentList.append(line)
        # print(contentList)
        # print(len(contentList))
        # contentList = contentList[:-1]
    return contentList


