import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


### get the raw data section####
raw_data = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/bitcoin_2010-07-27_2024-04-25.csv")
ADA = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/OHLCV_Binance_ADA-USDT_D20180417T040200UTC-D20240404T115959UTC_1min.csv")
BNB = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/OHLCV_Binance_BNB-USDT_D20171106T035400UTC-D20240404T115959UTC_1min.csv")
ETH = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/OHLCV_Binance_ETH-USDT_D20170817T040000UTC-D20240404T115959UTC_1min.csv")
SOL = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/OHLCV_Binance_SOL-USDT_D20200811T060000UTC-D20240404T115959UTC_1min.csv")
XRP = pd.read_csv("F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Sources Files/OHLCV_Binance_XRP-USDT_D20180504T081100UTC-D20240404T115959UTC_1min.csv")
print("Imported Done :)")

###  Simple preprocessing ###
df = raw_data.iloc[::-1]
df = df.reset_index()
df = df.drop(index = df[df['Volume'] == 0].index)
df = df.reset_index()
df = df[['Start', 'High', 'Low', 'Volume']]
BTC = df


ADA['timestamp'] = pd.to_datetime(ADA['timestamp'], unit='s')
BNB['timestamp'] = pd.to_datetime(BNB['timestamp'], unit='s')
ETH['timestamp'] = pd.to_datetime(ETH['timestamp'], unit='s')
SOL['timestamp'] = pd.to_datetime(SOL['timestamp'], unit='s')
XRP['timestamp'] = pd.to_datetime(XRP['timestamp'], unit='s')



### Exporting ###
BTC.to_csv('F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/BTC.csv',index=1)
for i,s in zip([ADA, BNB, ETH, SOL, XRP],['ADA', 'BNB', 'ETH', 'SOL', 'XRP']):
    tt = i.groupby(pd.to_datetime(i['timestamp']).dt.date)['high']
    
    tt = pd.DataFrame(tt.mean())
    tt.to_csv(f'''F:/Prjoects/BTC/04 US daily stock market prediction/ETL/Scripts out/{s}.csv''', index=1)
print("Exoporting Done -_^")