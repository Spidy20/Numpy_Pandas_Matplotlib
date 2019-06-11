import numpy as np
a = np.arange(9, dtype = np.float_).reshape(3,3)

print ('First array:' )
print (a )
print ('\n'  )

print ('Second array:' )
b = np.array([2,2,2])
print (b)
print ('\n'  )
#
print ('Add the two arrays:' )
print (np.add(a,b) )
print ('\n' )

print ('Subtract the two arrays:' )
print (np.subtract(a,b) )
print ('\n'  )

print ('Multiply the two arrays:' )
print( np.multiply(a,b) )
print ('\n')
#
print ('Divide the two arrays:' )
print (np.divide(a,b))