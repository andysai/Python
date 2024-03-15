# 之前input()输入的数据为str类型
start_floor = '3'
end_floor = '4'
floor_last_number = ['01','02','03']

#初始楼层的模版数据
start_floor_rooms = {301:[1,80], 302:[1,80], 303:[2,90]}

# 创建一个字典，存储所有楼层的数据
unit_rooms = {}

# unit_rooms = {3: {301: [1, 80], 302: [1, 80], 303: [2, 90]}}
unit_rooms[int(start_floor)] = start_floor_rooms

# 给4楼创建一个字典
floor_rooms = {}
#遍历每层有多少个房间，这里是3，即执行for i in range 3 的循环
for i in range(len(start_floor_rooms)):
    # 字符串拼接, number = ['401','402','403']
    number = '4' + floor_last_number[i]
    # 依次取出字典start_floor_rooms键对应的值，即面积和朝向组成的列表
    info = start_floor_rooms[int(start_floor + floor_last_number[i])]
    # int(start_floor + floor_last_number[0])= 301
    # info = [1,80]
    # 给字典floor_rooms添加键值对，floor_rooms = {401:[1,80]}
    # 循环三次，所以floor_rooms = {401:[1,80], 402:[1,80], 403:[2,90]}
    floor_rooms[int(number)] = info

# 以4为键，floor_rooms为值，给字典unit_rooms添加键值对
unit_rooms[int(end_floor)] = floor_rooms
# unit_rooms = {3: {301: [1, 80], 302: [1, 80], 303: [2, 90]}, 4: {401: [1, 80], 402: [1, 80], 403: [2, 90]}}
print(unit_rooms)
