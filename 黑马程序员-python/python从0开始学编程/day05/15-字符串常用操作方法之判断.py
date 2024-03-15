# isalpha():如果字符串至少有一个字符并且所有的字符都是仔面则返回True,否则返回False。
mystr1 = 'hello'
mystr2 = 'hello12345'
print(mystr1.isalpha())
print(mystr2.isalpha())

# isdigit():如果字符串只包含数字则返回True,否则返回False。
mystr1 = 'hello12345'
mystr2 = '123456'
print(mystr1.isdigit())
print(mystr2.isdigit())

# isalnum():如果字符串至少有一个字符并且所有字符都是字母或数字则返回True,否则返回False。
mystr1 = 'hello12345'
mystr2 = '123456'
print(mystr1.isalnum())
print(mystr2.isalnum())

# isspace():如果字符串只包含空白，则返回True,否则返回False。
mystr1 = '1 2 3 4 5'
mystr2 = '      '
print(mystr1.isspace())
print(mystr2.isspace())