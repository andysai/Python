from rediscluster import RedisCluster
import redis

r = redis.Redis(host='10.12.12.100', port=6379, password='dslr@2023', db=0)
r.set('hello2024', 'world2024')
print(r.get('hello2024'))

# from rediscluster import RedisCluster
# # 假设Redis集群节点的IP和端口信息如下
# startup_nodes = [
#     {"host": "10.244.224.112", "port": "6379"},
#     {"host": "10.244.224.237", "port": "6379"},
#     {"host": "10.244.224.77", "port": "6379"}
# ]
#
# # 连接到Redis集群
# rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, password='Dslr#2023@PoSTeST')
#
# # 设置键值对
# rc.set("foo", "bar")
#
# # 获取键的值
# value = rc.get("foo")
# print(value)  # 输出: bar
#
# # 关闭连接
# rc.connection_pool.disconnect()
