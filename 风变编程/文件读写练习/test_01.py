with open('a.txt','w',encoding='utf-8') as file:
    file.write('hello\n')

with open('a.txt','test_1',encoding='utf-8') as file:
    file.write('python\n')

with open('a.txt','r',encoding='utf-8') as file:
    a = file.readlines()
print(a)