# class Demo():
#     def __new__(cls, *args, **kwargs):
#         print("new class")
#
# d = Demo()

'''


class B():
    def fn(self):
        print('B fn')
    def __init__(self):
        print('B init')

class A():
    def fn(self):
        print('A fn')
    def __new__(cls, a):
        print('new',a)
        if a > 10 :
            return super(A,cls).__new__(cls)
        return B()
    def __init__(self,a):
        print('init',a)


a1 = A(5)
a1.fn()
a2 = A(15)
a2.fn()

'''
'''
class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        super().__init__()

class C(A):
    def __init__(self):
        print('C')
        super().__init__()
class D(B,C):
    def __init__(self):
        print('D')
        super().__init__()

d = D.mro()
print(d)
print(C.__mro__)
'''

from xpinyin import Pinyin


import os

print(os.path.dirname(__file__))

# with open('hanzi.txt','a') as f:
#     f.write('焦鑫磊')
#
# p = Pinyin()
# pinyin = p.get_pinyin('焦鑫磊真是个大帅比',' ',tone_marks='marks')
#
# print(pinyin)









