def user_info(name, age, gender='男'):
    print(f'您的姓名是{name}，年龄是{age},性别是{gender}')

user_info('TOM',18)
user_info('ROSE',20,'女')
user_info('ROSE',20,gender='女')