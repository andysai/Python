# 需求:通过信息节点或端口号判断网线在交换机的哪个端口
# 2.1 信息节点查询端口
def Query_information():
    Information_point = int(input("请输入信息节点:"))
    if Information_point > 0 and Information_point <= 49:
        position = Information_point - 1 + 1
        print(f'该信息节点在第一台交换机，对应端口号为:{position}')
    elif Information_point > 49 and Information_point <= 96:
        position = Information_point - 49 + 1
        print(f'该信息节点在第二台交换机，对应端口号为:{position}')
    elif Information_point > 96 and Information_point <= 144:
        position = Information_point - 96 + 1
        print(f'该信息节点在第三台交换机，对应端口号为:{position}')
    elif Information_point > 144 and Information_point <= 192:
        position = Information_point - 144 + 1
        print(f'该信息节点在第四台交换机，对应端口号为:{position}')
    elif Information_point > 192 and Information_point <= 240:
        position = Information_point - 192 + 1
        print(f'该信息节点在第五台交换机，对应端口号为:{position}')
    else:
        print('请输入正确的信息节点!')

# 2.2 端口号查询信息点
def switch_port_message():
    switch = int(input("请输入交换机编号:"))
    Port_number = int(input("请输入交换机端口号:"))
    if (Port_number >= 1 and Port_number <= 48) and switch == 1:
        position = Port_number
        print(f'信息点为{position}')
    elif (Port_number >= 1 and Port_number <= 48) and switch == 2:
        position = Port_number + 49 - 1
        print(f'信息点为{position}')
    elif (Port_number >= 1 and Port_number <= 48) and switch == 3:
        position = Port_number + 144 - 1
        print(f'信息点为{position}')
    elif (Port_number >= 1 and Port_number <= 48) and switch == 4:
        position = Port_number + 192 - 1
        print(f'信息点为{position}')
    elif (Port_number >= 1 and Port_number <= 48) and switch == 5:
        position = Port_number + 193 - 1
        print(f'信息点为{position}')
    else:
        print("请输入正确的交换机编号和端口号")


# 1. 定义用户须输入的参数
def use_chooise():
    a = True
    while a:
        chooise = input("请选择是通过信息点还是通过端口号查找信息(1 信息节点 or 2 端口号 or q 退出脚本 ):")
        if chooise == '1':
            Query_information()
        elif chooise == '2' :
            switch_port_message()
        elif chooise == 'q':
            print("退出脚本")
            a = False
        else:
            print("请按照提示进行选择!")

# 3. 调用函数
if __name__ == '__main__':
    use_chooise()