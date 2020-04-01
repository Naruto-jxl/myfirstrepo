# import redis
#
# # print(dir(redis.Redis))
#
# pool = redis.ConnectionPool(host='127.0.0.1',port=6379)                 #连接池
# redis_instance = redis.Redis(connection_pool=pool)                      #通过连接池创建实例，避免了不断新建释放的开销
# # redis_instance = redis.Redis(host='127.0.0.1',port=6379)              #直接新建redis实例，不通过连接池，开销大
#
# redis_instance.set('jxldemo',15)
# num = redis_instance.get('jxldemo')
# redis_instance.incr('jxldemo',5)
# num2 = redis_instance.get('jxldemo')
# print(type(num))
# print(num)
# print(num2)

# from queue import Queue
#
# q = Queue()
#
# print(dir(q))
#
# q.put(1)
# q.put(2)
# q.put(3)
# for i in range(3):
#     result = q.get()
#     print(result)



