###Take array for mathamatical calculation
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print ('Shape-',a.shape)
print('Array 2*3-',a)  ####2 -for row & 3 for column

# ##Change the shape
a.shape = (3,2)
print('3*2',a)

# ###Reshape function
c = np.array([[1,2,3],[4,5,6]])
d = c.reshape(3,2)
print ('After reshape-',d)
#
##create & arrange array
e = np.arange(24)
print(e)
f=e.reshape(2,4,3)
print(f)