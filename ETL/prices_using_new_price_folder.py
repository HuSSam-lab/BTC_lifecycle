import pandas as pd


####### BTC
BTC = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/New Prices/BTC_2010-07-17_2024-05-16.csv")
BTC_features = ['Start', 'High', 'Low', 'Volume']
BTC = BTC[BTC_features]
# BTC.rename(columns = {'Start' : 'date'}, inplace=True)
BTC['Start'] = pd.to_datetime(BTC['Start'])


BTC = BTC[::-1]
BTC.reset_index(inplace=True, drop=True)
BTC.to_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/BTC.csv', index=1, index_label='index')

######## other curr
ADA = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/New Prices/ADA_2017-10-01_2024-05-16.csv")
BNB = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/New Prices/BNB_2017-08-16_2024-05-16.csv")
ETH = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/New Prices/ETH_2015-08-07_2024-05-16.csv")
SOL = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/New Prices/SOL_2020-04-09_2024-05-16.csv")
XRP = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/New Prices/XRP_2013-08-16_2024-05-16.csv")

ADA['date'] = pd.to_datetime(ADA['Start'])
BNB['date'] = pd.to_datetime(BNB['Start'])
ETH['date'] = pd.to_datetime(ETH['Start'])
SOL['date'] = pd.to_datetime(SOL['Start'])
XRP['date'] = pd.to_datetime(XRP['Start'])

features = ['date', 'High']

for i,s in zip([ADA, BNB, ETH, SOL, XRP],['ADA', 'BNB', 'ETH', 'SOL', 'XRP']):
    i[features].to_csv(f'''F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/{s}.csv''', index=0)