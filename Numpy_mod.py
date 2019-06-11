import numpy as np
a = np.array([10,20,30])
b = np.array([2,5,3])

print ('First array:' )
print (a)
print ('\n')

print ('Second array:' )
print (b)
print ('\n')

print ('Applying mod() function:' )
print (np.mod(a,b))
print ('\n')

print ('Applying remainder() function:' )
print (np.remainder(a,b))