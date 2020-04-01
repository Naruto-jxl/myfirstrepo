# import os
#
# dirname = os.path.dirname(__file__)
# for file in os.listdir(dirname):
#     print(file)
'''



import threading
import time
class BaseClass(object):
    _lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not hasattr(BaseClass,'_instance'):
            with BaseClass._lock:
                if not hasattr(BaseClass, '_instance'):
                    BaseClass._instance = object.__new__(cls)
        return BaseClass._instance
    def __init__(self,name):
        self.name = name
        time.sleep(1)
'''
#
# def task(name):
#     obj = BaseClass(name)
#     print(obj.name,obj)
# #
# for i in ['a','b','c','d','e','f']:
#     t = threading.Thread(target=task,args=(i,))
#     t.start()
#     time.sleep(5)
#
#
# task('jxl')
# task('aaa')

# a = BaseClass('jxl')
# b = BaseClass('aaa')
# print(a.name)
# print(b.name)


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

#
# a1 = A(2)
# a2 = A(3)
# print(a1.x)
# print(a2.x)



def singleton(cls):
    _instance = {}
    def inner(*args,**kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]
    return inner


@singleton                  #装饰器实现单例模式
class DemoClass(object):
    def __init__(self,name):
        self.name = name

a1 = DemoClass('jxl')
a2 = DemoClass('ztd')
a3 = DemoClass('wc')
print(a1.name,a1)
print(a2.name,a2)
print(a3.name,a3)

