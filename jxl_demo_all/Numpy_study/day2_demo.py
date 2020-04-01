# a = 'hello'
# b = b'hello'
# print(type(a))
# print(type(b))      #<class 'bytes'>
# print(b[0:5])
#
# print(ord('h'))
# print(chr(104))

import numpy as np

array = np.arange(9).reshape(3,3)
print(array)
print()
# print(array[1,2])
# print(array[...,2])
# print(array[1,...])
# print(array[[1,2],...])
# print(array[[0,0,2,2],[0,2,0,2]].reshape(2,2))
#
# rows = np.array([[0,0],[2,2]])
# cols = np.array([[0,2],[0,2]])
# print('rows',rows)
# print('cols',cols)
#
# print('--------------')
# print(array[rows,cols])
# print(array[array < 6])         #取出小于6的元素









