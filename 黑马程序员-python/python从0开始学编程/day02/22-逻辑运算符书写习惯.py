a = 0
b = 1
c = 2

# 1 and:与
print((a < b) and (c > b))
print((a > b) and (c > b))

# 2 or: 或
print((a < b) or (c > b))
print((a > b) or (c > b))
print((a > b) or (c < b))

# 3 not: 非
print(not False)
print(not True)
print(not (c > b))