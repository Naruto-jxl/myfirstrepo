from numpy import array


ndarray = array([[[1],[0]],[[2],[3]],[[4],[5]],[[6],[7]]])
# print(ndarray)
'''
[[1 0]
 [2 3]
 [4 5]]
'''
print(ndarray.size)         #数组元素总个数
print(ndarray.ndim)         #数组维数，秩
print(ndarray.shape)        #数组维度，也就是每个轴上的元素数量
print(ndarray.dtype)
print(ndarray.itemsize)     #数组元素的大小（单位：字节）

b = ndarray.reshape(2,4)    #reshape()方法可以修改数组的维度
ndarray.shape = (2,4)       #或者直接给原维度赋值
print(b)
print(ndarray)





