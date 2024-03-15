file1 = open('abc.txt','r',encoding='utf-8')
filecontent = file1.read()
print(filecontent)
file1.close()

file2 = open('a.txt','test_1',encoding='utf-8')
file2.write('张无忌\n')
file2.write('宋青书\n')
file1.close()