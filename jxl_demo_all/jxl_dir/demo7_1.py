import os

dir_list = dir(os)

# with open('osdir.txt','w') as f :
#     for i in dir_list:
#         f.write(i)
#         f.write(' ')

# with open('osdir.txt','r') as f:
#     astr = f.read()
#     alist = astr.split()
#     blist = [i for i in alist if 'dir' in i]
#     print(blist)


# alist = os.listdir('../jxl_dir')
# print(alist)

# with open('demodir.txt','w') as f:
#     with open('osdir.txt','r') as f1:
#         astr = f1.read(4)
#         while astr != '':
#             f.write(astr+'\n')
#             astr = f1.read(4)

import time
alist = (i for i in range(5))

while True:
    try:
        print(next(alist))
    except StopIteration :
        print('数据取完了')
        break
    time.sleep(1)



