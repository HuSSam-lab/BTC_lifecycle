import pandas as pd

r_WW = pd.read_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/Trend/BTC Trend worldWide.csv',header=1)
r_US = pd.read_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/Trend/BTC Trend US.csv',header=1)
r_GR = pd.read_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/Trend/BTC Trend Germany.csv',header=1)
r_UAE = pd.read_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/Trend/BTC Trend UAE.csv',header=1)
r_dubai = pd.read_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/Trend/BTC Trend Dubai.csv',header=1)
print('imported Done :)')
################################### 1
r_US.drop(['Month'], axis = 1, inplace=True)
r_GR.drop(['Month'], axis = 1, inplace=True)
r_UAE.drop(['Month'], axis = 1, inplace=True)
r_dubai.drop(['Month'], axis = 1, inplace=True)
df = pd.concat([r_WW, r_US, r_GR, r_UAE, r_dubai],axis=1)
to = ['date','worldwide', 'unitedstates', 'Germany', 'UAE', 'Dubai']
df = df.set_axis(to,axis = 1)
###################################  2
to.remove('date')
df.replace('<1','0',inplace=True)
# print(df['worldwide'].unique())
################################### 3
df['date'] = [pd.to_datetime(i).date() + pd.DateOffset(days= 0) for i in df['date'] ]
###################################
df.to_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/Google Trend.csv', index=0)
print('Exported Done ^_-')