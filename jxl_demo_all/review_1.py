'''


adict = {'a':1}
num = adict.setdefault('b',2)
# print(num)
# num2 = adict.get('c')
# print(num2)
num2 = adict.pop('a')
print(adict)
print(num2)
'''
'''


class Atest():
    name = '焦鑫磊'
    def getname(self):
        return '程序猿'

a = Atest()
print(hasattr(a,'name'))
delattr(Atest,'name')
print(hasattr(a,'name'))
setattr(Atest,'age',18)
print(getattr(Atest,'age'))
'''
#
# adict = {123:'jxl'}
# print(adict)

import json
import pandas
import xlwt
# alist = ['name','age','hobby']
# json_alist = json.dumps(alist)
#
# print(json_alist)

# blist = [{'name':'jxl','age':18,'gender':'男'},{'name':'焦鑫磊','gender':'男'}]
# blist_json = json.dumps(blist)
# data = pandas.read_json(blist_json)
# point_data = data.to_excel('info.xls')


# import re
#
# astr = 'hello world hello python'
# result = re.findall(r'(?<!world )hello(?! python)',astr)
# print(result)
#
# import logging

# aset = {1,2,3,4}
# bset = {6,2,7,4}
# result = aset&bset
# result2 = aset | bset
#
# print(result)
# print(result2)

'''
插入排序

def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        tmp = alist[i]
        j = i
        while j > 0 :
            if tmp < alist[j-1]:
                alist[j] = alist[j-1]
            else:
                break
            j -= 1
        alist[j] = tmp
    return alist

print(insert_sort([3,6,4,7,9,12,8]))
'''


# alist = [2,4,1,3,5,7,8,15]
#
# alist1 =[2,4,1,3,5]
#
# alist2 =[7,8,15]
#
# res = sorted(alist)
# print(res)
# from collections.abc import Iterable
# print(isinstance(alist,Iterable))
# alist = [
#     {'name':'jxl','age':18},
#     {'name':'jxl2','age':15},
#     {'name':'jxl3','age':10}
# ]
# print(sorted(alist,key=lambda x:x['age']))


# adict = {'name':'jxl','age':19}
# print(adict.items())




'''
查询语句
索引
'''

# import time,functools
# #
# def out_func(func):
#     print(func.__name__)
#     @functools.wraps(func)
#     def inner(*args,**kwargs):
#         print(func.__name__)
#         now = time.time()
#         res = func(*args,**kwargs)
#         now_new = time.time()
#         deltatime = now_new-now
#         print(deltatime)
#         return res
#     return inner
#
# @out_func
# def add(x,y):
#     time.sleep(2)
#     return x+y
#
# print(add(3,6))

# def extendlist(val, list=[]):
#     list.append(val)
#     return list
# list1 = extendlist(10)
# print(list1)
# list2 = extendlist(123, [])
# print(list1)
# list3 = extendlist('a')
# print(list1)
# print("list1 = %s" %list1)
# print("list2 = %s" %list2)
# print("list3 = %s" %list3)


# numbers = [1, 2, 3, 4, 5, 6,7,8]
#
# for n in numbers:
#     numbers.remove(n)
#     print(numbers)

# print('{1},{0}'.format('hello','python'))
# print(dict([]))


# def add(x=10):
#     x += 5
#     return x
#
# a = add()
# b = add()
# print(a)
# print(b)
#
#
# def change_alist(alist=[]):
#     alist.append(10)
#     return alist
#
# print(change_alist())
# print(change_alist())


def feibo(n):
    if n==1 or n==2:
        return 1
    return feibo(n-1)+feibo(n-2)

print(5)

def feibo_generator(n):
    a,b = 1,1
    for i in range(n):
        c = a
        a,b = b,a+b
        yield c
print(list(feibo_generator(5)))