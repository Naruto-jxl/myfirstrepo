# print('hello{}hello{}'.format('world','python'))
# print('你好%s你好%s'%('人间','世界'))
'''


#冒泡排序
class BubbleSort():
    def run(self,alist):
        n  = len(alist)
        for i in range(1,n):
            for j in range(0,n-i):
                if alist[j] > alist[j+1]:
                    alist[j],alist[j+1] = alist[j+1],alist[j]
        return alist

alist = [2,3,1,4,6,3,8,7,5]
blist = BubbleSort()
print(blist.run(alist))

'''
#选择排序

class ChooseSort():
    def run(self,alist):
        n = len(alist)
        for i in range(0,n):
            x = i
            for j in range(i+1,n):
                if alist[j] < alist[x]:
                    x = j
            if x != i:
                alist[i],alist[x] = alist[x],alist[i]
        return alist

c = ChooseSort()
print(c.run([3,6,9,7,5,8,4]))









