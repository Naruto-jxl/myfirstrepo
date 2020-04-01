# import re
# astr = '$239.99'
#
# result = re.findall(r'([$A-Z]+)(\d.*)',astr)
# print(result)

# import random
# alist = [random.randint(1,100) for i in range(10)]
# print(alist)


'''

subquery_result = session.query(d,func.count(1).label('num')).filter(and_(d.id==a.id,d.user_id==a.user_id)).subquery()

result = session.query(a.id).join(b,a.id=b.a_id).filter(and_(subquery_result.c.num==0,a.year>2010)).limit(group_size).all()


'''

# def best_profit(alist):
#     n = len(alist)
#     profit_total = []   #所有的买卖利润数据列表，包括盈亏
#     for i in range(n-1):
#         blist = alist[i+1:n]
#         profit = list(map(lambda x:x-alist[i],blist))       #假设当前时刻买入，并在以后的任何时刻出售，所能获得的盈亏利润数据列表
#         profit_total += profit                              #将所有利润数据汇总，返回最大值。该算法的缺点是只有收益，没有买卖时刻
#     print(profit_total)
#     return max(profit_total)
#
# alist = [10,7,5,8,11,9]
# print(best_profit(alist))



# import datetime
#
# def func(date_time):
#     start_time = datetime.datetime.strptime('1990-01-01','%Y-%m-%d')
#     try:
#         date_time = datetime.datetime.strptime(date_time,'%Y-%m-%d')
#     except ValueError:
#         return '非法输入'
#     if date_time < start_time:
#         return '非法输入'
#     time_delta = (date_time-start_time).days
#     # print(time_delta)
#     ret = time_delta%5
#     if 1 <= ret <=3:
#         return '打鱼'
#     else:
#         return '晒网'
#
#
# print(func(input('请输入时间')))


#
# def snake_func(num):
#     if num > 100:
#         return
#     tmp_begin = 1
#     for i in range(1, num+1):
#         begin = tmp_begin
#         if i == num:
#             print(begin)
#         else:
#             print(begin, end=" ")
#         for j in range(i+1, num+1):
#             begin += j
#             if j == num:
#                 print(begin)
#             else:
#                 print(begin, end=" ")
#         tmp_begin += i
#
# num = int(input())
# snake_func(num)

def func(num,s):
    for i in range(num):
        s += i
        s1 = s
        for j in range(1,num+1-i):

            if j == 1:
                print(s,end=' ')
            else:
                s1 += i+j
                print(s1,end=' ')
        print()

func(5,1)



