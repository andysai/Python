TT = []
def ubuntu():
    Data = []
    IP = []
    Version = []
    Kernel = []
    with open('ubuntu.log', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in lines:
            Data.append(i.strip())

    for i in range(0, len(Data)+1, 3):
        if i < len(Data):
            IP.append(Data[i].split('|')[0].strip())
        else:
            break

    for j in range(1, len(Data)+1, 3):
        if j <= len(Data):
            Version.append(Data[j].split('\\n')[0].strip())
        else:
            break

    for k in range(2, len(Data)+1, 3):
        if k <= len(Data):
            Kernel.append(Data[k])
        else:
            break

    for i in range(0, len(IP)+1):
        if i < len(IP):
            IP_list = IP[i]
            Version_list = Version[i]
            Kernel_list = Kernel[i]
            print([IP[i], Version[i], Kernel[i]])
            TT.append([IP[i], Version[i], Kernel[i]])
        else:
            break


ubuntu()
print(TT)
