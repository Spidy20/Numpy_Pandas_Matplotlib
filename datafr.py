##Create dataframe in python

##create dataframe using dictionary
import pandas as pd
data = {'Name':['Kushal', 'Ashok', 'Monika', 'Tasha'],'Age':[18,24,20,20]}
df = pd.DataFrame(data)

dt = pd.read_csv('info.csv')
print(dt)


##create a dataframe using list using dictionary
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
ef = pd.DataFrame(data, index=['first', 'second'])
ef.to_csv('tr.csv')
print (ef)
#
##create a dataframe using only list
data = [['Kushal',18],['Tasha',20],['Ashok',24]]
kf = pd.DataFrame(data,columns=['Name','Age'])