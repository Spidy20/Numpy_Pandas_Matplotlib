# -*- coding: utf-8 -*-
"""
@author: kusha
"""
#### simple line plotting with pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
df.plot()
df.plot()
# =============================================================================
###using matplotlib

plt.plot(df)
# =============================================================================

####Lets see a Bar plot
kf = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
kf.plot.bar()


##To produce a stacked bar plo
kf.plot.bar(stacked=True)

###To get horizontal bar plots
kf.plot.barh()


####Draw a Histogram
ef = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
ef.plot.hist(bins=20)

###For area plot
f = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
f.plot.area()

###Box plot
kk = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
kk.plot.box()


####Scatter plot
l = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
l.plot.scatter(x='a', y='b')


###Pie plot
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)

