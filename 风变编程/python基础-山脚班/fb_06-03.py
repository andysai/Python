while True:
    a = str(input('A，你认罪吗？请回答认罪或者不认'))
    b = str(input('B，你认罪吗？请回答认罪或者不认'))
    if a!='认罪' and b!='认罪':
        print('各判十年')
    elif a!='认罪' and b=='认罪':
        print('A20年，B1年')
    elif a=='认罪' and b!='认罪':
        print('A1年，B20年')
    else:
        print('各判三年')
        break