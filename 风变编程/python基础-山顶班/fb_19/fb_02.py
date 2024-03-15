start_floor = '3'
start_floor_rooms = {301:[1,80],302:[1,80],303:[2,90]}
#初始楼层的数据

unit_rooms = {}
#创建一个存放单元所有楼层数据的字典
unit_rooms[start_floor] = start_floor_rooms
print(unit_rooms)