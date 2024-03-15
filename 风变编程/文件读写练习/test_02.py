with open('a.txt','r',encoding='utf-8') as file:
    a = file.readlines()
    print(a)
    with open('a.txt','test_1',encoding='utf-8') as file1:
        file1.write('test\n')
print(a)