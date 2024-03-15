# 2. 可变类型：列表
aa = [10, 20]
bb = aa

print(bb)

print(id(aa)) # 1284727657032
print(id(bb)) # 1284727657032

aa.append(30)
print(aa)
print(bb) # 列表是可变类型

print(id(aa)) # 1284727657032
print(id(bb)) # 1284727657032