import numpy as np
a = np.array([1, 256, 8755], dtype = np.int16)

print ('Our array is:' )
print (a)

print ('Representation of data in memory in hexadecimal form:'  )
print (map(hex,a)  )
# byteswap() function swaps in place by passing True parameter

print ('Applying byteswap() function:' )
print (a.byteswap(True) )

print ('In hexadecimal form:' )
print (map(hex,a) )