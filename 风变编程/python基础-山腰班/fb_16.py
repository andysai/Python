# 先补全代码，然后再运行。
# 可体会多重继承中的就近原则。
class Teacher:
    face = 'serious'
    job = 'teacher'

class Father:
    face = 'sweet'
    parenthood = 'dad'

class Student(Teacher):
    pass

class Son(Father):
    face = 'gentle'

time3 = Student()
time4 = Son()
print(time3.face)
print(time4.face)