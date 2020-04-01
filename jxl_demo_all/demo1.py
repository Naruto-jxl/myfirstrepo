class Demo():
    __fields = '壮壮'

    def __init__(self):
        self.__attr = '二二'


    @classmethod
    def method1(cls):
        print(cls.__fields)         #类私有属性可以在类内部进行调用
        print(cls.__name__)
        print(hasattr(cls, '_'+cls.__name__+'__fields'))            #查看私有属性需要使用格式 ‘_类名__私有属性’
        print(hasattr(cls, '__fields'))                             #直接查看__私有属性会报错

    def method2(self):
        print(Demo.__fields)
        print(hasattr(Demo,'_Demo__fields'))
        print(getattr(self,'__attr'))                   #错误用法
        print(getattr(self,'_Demo__attr'))              #正确用法

Demo.method1()

a = Demo()
a.method2()
