import asyncio
import time
# print(dir(asyncio))
# print(help(time))
now = lambda :time.time()
# print(now())
async def do_some(t):        #使用async 定义一个协程
    print('hello world %s'%t)
    await asyncio.sleep(t)      #使用asyncio.sleep()来模拟耗时的I/O操作
    return 'task_result_%s'%t
#定义回调函数，在task执行期间执行,参数是future代表即将执行的任务
def callback(future):
    print(future.result())      #通过future.result()可以获取协程task执行结果

start = now()
tasks = []
for i in range(2,5):
    coroutine = do_some(i)
    tasks.append(asyncio.ensure_future(coroutine))     #创造多个协程，模拟并发

loop = asyncio.get_event_loop()         #建一个事件loop
# loop.run_until_complete(coroutine)      #将协程加入事件循环loop
# task = loop.create_task(coroutine)        #使用自定义事件循环loop创建task
# task = asyncio.ensure_future(coroutine)     #使用asyncio.ensure_future()创建task，效果和上面一样
# print('创建task--%s'%task)
# task.add_done_callback(callback)            #调用回调函数，注意这个操作不能放在下边的task执行之后再运行，获取不到task结果
# print('调用回调函数后--%s'%task)

loop.run_until_complete(asyncio.wait(tasks))    #执行时间循环loop，也就是执行异步任务
print(asyncio.Task.all_tasks(loop))
for t in tasks:
    print('运行结果%s'%t.result())
# print('执行结束后--%s'%task)
print(now()-start)









