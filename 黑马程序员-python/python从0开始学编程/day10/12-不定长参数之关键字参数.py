# 收集所有的关键字参数，返回一个字典

def user_info(**kwargs):
    print(kwargs)

# {'name':'TOM','age':18,'id':110}
#user_info()
#user_info(name='TOM')
#user_info(name='TOM',age=20)
user_info(name='TOM',age=20,id=110)