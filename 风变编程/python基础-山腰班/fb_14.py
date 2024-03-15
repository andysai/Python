class C0:
    name = 'C0'

class C1:
    num = 1

class C2(C0):
    num = 2

class C3:
    name = 'C3'

class C4(C1,C2,C3):
    pass

mess = C4()
print(mess.name)
print(mess.num)