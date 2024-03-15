# 拆包：字典
dict = {'name':'TOM','age':20}

a,b = dict
print(a) # name
print(b) # age

a,b = dict.keys()
print(a) # name
print(b) # age

a,b = dict.values()
print(a) # TOM
print(b) # 20