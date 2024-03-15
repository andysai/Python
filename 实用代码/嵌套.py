def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x+5

add = apply_twice(add_five, 10)

print(add)

