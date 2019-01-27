import numpy as np
from scipy import stats
dataset= [1,1,2,3,4,6,18]

##Mean: - Sum of elements / elements number

#mean value
mean= np.mean(dataset)

#median value
median = np.median(dataset)

#mode value
mode= stats.mode(dataset)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)


