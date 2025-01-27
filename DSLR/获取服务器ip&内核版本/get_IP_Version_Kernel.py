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
            TT.append([IP[i], Version[i], Kernel[i]])
        else:
            break

def suse11():
    Data = []
    IP = []
    Version = []
    Kernel = []
    with open('suse11.log', 'r', encoding='utf-8') as f:
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
            Version.append(Data[j].split('Welcome to ')[1].split('(x86_64)')[0].strip())
        else:
            break

    for k in range(2, len(Data)+1, 3):
        if k <= len(Data):
            Kernel.append(Data[k])
        else:
            break

    for i in range(0, len(IP)+1):
        if i < len(IP):
            TT.append([IP[i], Version[i], Kernel[i]])
        else:
            break

def suse12():
    Data = []
    IP = []
    Version = []
    Kernel = []
    with open('suse12.log', 'r', encoding='utf-8') as f:
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
            Version.append(Data[j].split('Welcome to ')[1].split('(x86_64)')[0].strip())
        else:
            break

    for k in range(2, len(Data)+1, 3):
        if k <= len(Data):
            Kernel.append(Data[k])
        else:
            break

    for i in range(0, len(IP)+1):
        if i < len(IP):
            TT.append([IP[i], Version[i], Kernel[i]])
        else:
            break

def rhel5():
    Data = []
    IP = []
    Version = []
    Kernel = []
    with open('rhel5.log', 'r', encoding='utf-8') as f:
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
            Version.append(Data[j])
        else:
            break

    for k in range(2, len(Data)+1, 3):
        if k <= len(Data):
            Kernel.append(Data[k])
        else:
            break

    for i in range(0, len(IP)+1):
        if i < len(IP):
            TT.append([IP[i], Version[i], Kernel[i]])
        else:
            break

def rhel6():
    Data = []
    IP = []
    Version = []
    Kernel = []
    with open('rhel6.log', 'r', encoding='utf-8') as f:
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
            Version.append(Data[j])
        else:
            break

    for k in range(2, len(Data)+1, 3):
        if k <= len(Data):
            Kernel.append(Data[k])
        else:
            break

    for i in range(0, len(IP)+1):
        if i < len(IP):
            TT.append([IP[i], Version[i], Kernel[i]])
        else:
            break

def centos6():
    Data = []
    IP = []
    Version = []
    Kernel = []
    with open('centos6.log', 'r', encoding='utf-8') as f:
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
            Version.append(Data[j])
        else:
            break

    for k in range(2, len(Data)+1, 3):
        if k <= len(Data):
            Kernel.append(Data[k])
        else:
            break

    for i in range(0, len(IP)+1):
        if i < len(IP):
            TT.append([IP[i], Version[i], Kernel[i]])
        else:
            break

def centos7():
    Data = []
    IP = []
    Version = []
    Kernel = []
    with open('centos7.log', 'r', encoding='utf-8') as f:
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
            Version.append(Data[j])
        else:
            break

    for k in range(2, len(Data)+1, 3):
        if k <= len(Data):
            Kernel.append(Data[k])
        else:
            break

    for i in range(0, len(IP)+1):
        if i < len(IP):
            TT.append([IP[i], Version[i], Kernel[i]])
        else:
            break

ubuntu()
suse11()
suse12()
rhel5()
rhel6()
centos6()
centos7()
