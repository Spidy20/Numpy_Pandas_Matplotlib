import quandl

quandl.ApiConfig.api_key = 'cEwafLSxcxfDwzNREWup'
t = quandl.get('NSE/ICICIBANK')


import pandas as pd
df = pd.DataFrame(t)
df.to_csv('icici.csv')
print('CSV created')