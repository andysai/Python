Ec_App_lists = []
with open("2022-07-29.txt", 'r') as f:
    readlines = f.readlines()
    for i in readlines:
        Ec_App_lists.append(i.strip())


for Ec_App_list in Ec_App_lists:
    print(Ec_App_list, end=" ")


