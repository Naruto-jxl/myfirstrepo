# import re
# astr = '<table>this is table</table><name>this is name</name>'
#
# result = re.findall(r'<([a-zA-Z]+)>',astr)
# print(result)

# def func(a=[]):
#     a.append(1)
#     print(a)
#
# func()
# func([2])
# func()

# while True:
#     num = input('请输入数字')
#     if not num.isdigit() or 1<=int(num)<=100:
#         print('error')

# adict = {'name':'jxl','age':18}
#
# age = adict.pop('age')

# astr = 'abcdefg'
# new_astr = sorted(astr,reverse=True)
# print(new_astr)


# alist = ['name1','name2','name3']
# alist2 = ['jxl','jxl2','jxl3']
#
# result = zip(alist,alist2)
# print(dict(result))


# aset = set()
# aset.add(1)
# print(aset)

#每周30节课，一共210节课，一共7周，假设日期是2020-3-13

import datetime
from datetime import timedelta
startdate = datetime.datetime.strptime('2020-3-13','%Y-%m-%d')
enddate = startdate+timedelta(days=1)
# print(enddate)
def enddatetime(n):
    return startdate+timedelta(days=n)

alist = []
for i in range(7):
    if i==0:
        alist = [[startdate,enddatetime(1),enddatetime(2),enddatetime(3),enddatetime(4)]]
    else:
        alist.append([alist[i-1][0]+timedelta(days=7),alist[i-1][1]+timedelta(days=7),alist[i-1][2]+timedelta(days=7),alist[i-1][3]+timedelta(days=7),alist[i-1][4]+timedelta(days=7)])

for i in alist:
    for j in range(5):
        i[j] = i[j].strftime('%Y-%m-%d')
print(alist)











