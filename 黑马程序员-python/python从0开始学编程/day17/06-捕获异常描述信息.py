try:
    # print(1/0)
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)