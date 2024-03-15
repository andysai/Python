dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print(sorted(dict1.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))


