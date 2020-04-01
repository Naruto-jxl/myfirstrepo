
# def func1(n):
#     if n == 1:
#         return 1
#     return func1(n-1)+n
#
# print(func1(50))
#
#
# def func2(n):
#     if n == 1 :
#         return 1
#     return func2(n-2)+1/n
#
# print(func2(5))

# f = open('day7.txt','w')
# f.close()
# with open('day7.txt','r') as f:
#     # f.write('hello world')
#     astr = f.read(4)
#     print(astr)
#     bstr = f.read()
#     print(bstr)
import os

print(os.getcwd())              #C:\Users\64915\Desktop\jxl_demo_all
# os.mkdir('jxl_dir')
alist = dir(os)

os.chdir('jxl_dir')         #C:\Users\64915\Desktop\jxl_demo_all\jxl_dir
# print(os.getcwd())

with open('demo7_1.py','w') as f:
    f.write('import os')





