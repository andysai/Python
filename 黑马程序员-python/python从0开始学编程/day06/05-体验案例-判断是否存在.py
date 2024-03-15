name_list = ['Tom','Lily','Rose']

"""
1 用户输入账号
2 判断if...else
"""
name = input('请输入您邮箱账号:')

if name in name_list:
    print(f'您输入的账号{name}已经存在，请重新输入')
else:
    print(f'您的输入的账号{name}可以注册')