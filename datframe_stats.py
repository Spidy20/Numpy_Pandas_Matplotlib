import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print (df)

###For sum
sm=df.sum()
print(sm)

# =============================================================================
###For mean
mn=df.mean()
print('mean is:',mn)
#
##median
md=df.median()
print('median is',md)
# #
#
sd=df.std()
print(sd)
#
descr= df.describe()
print(descr)